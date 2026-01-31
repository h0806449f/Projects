import pandas as pd
import ipaddress
import textwrap

# ---------------------------------------
# 找出可用子網 & 重疊的子網（純 Python）
# ---------------------------------------
def find_available_cidrs(pool_cidr, desired_prefix, used_cidrs):
    """
    pool_cidr: 字串，例如 "10.10.0.0/19"
    desired_prefix: 整數，例如 22
    used_cidrs: 已使用 CIDR 列表，例如 ["10.10.16.0/22", "10.10.20.0/22"]
    """

    pool_net = ipaddress.IPv4Network(pool_cidr, strict=False)

    # ===【修正點 1】安全解析 used CIDR ===
    used_networks = []
    invalid_cidrs = []

    for cidr in used_cidrs:
        try:
            used_networks.append(ipaddress.IPv4Network(cidr, strict=False))
        except ValueError:
            invalid_cidrs.append(cidr)

    if invalid_cidrs:
        print("⚠️ 以下 CIDR 無法解析，已忽略：")
        for c in invalid_cidrs:
            print(f"  - {c}")
        print()

    available_cidrs = []
    overlapping_cidrs = []

    # 找出與 pool 有重疊的已使用網段
    for used in used_networks:
        if pool_net.overlaps(used):
            overlapping_cidrs.append(str(used))

    # 遍歷 pool 裡的所有 candidate 子網
    for subnet in pool_net.subnets(new_prefix=desired_prefix):
        if not any(subnet.overlaps(used) for used in used_networks):
            available_cidrs.append(str(subnet))

    return available_cidrs, overlapping_cidrs


# ---------------------------------------
# 主程式
# ---------------------------------------
def main():
    # 讀 CSV
    df = pd.read_csv("existing_vpcs.csv")

    if 'VpcCidr' not in df.columns:
        raise ValueError("CSV 欄位必須包含 'VpcCidr'")

    # ===【修正點 2】正確拆解 CSV 內多 CIDR 欄位 ===
    used_cidrs = []

    for cell in df['VpcCidr'].dropna():
        # 支援格式: "10.12.76.0/22, 10.8.128.0/17"
        parts = [c.strip() for c in str(cell).split(",")]
        for cidr in parts:
            if cidr:
                used_cidrs.append(cidr)

    # 設定 pool 與子網大小
    pool_cidr = "10.0.0.0/16"
    desired_prefix = 20

    # 計算可用子網 & 重疊子網
    available_cidrs, overlapping_cidrs = find_available_cidrs(
        pool_cidr,
        desired_prefix,
        used_cidrs
    )

    print(f"CIDR Pool 範圍: {pool_cidr}\n")
    print(f"希望切分的範圍: /{desired_prefix}\n")
    print(f"與 CIDR Pool 重疊的 CIDR:")
    for c in overlapping_cidrs:
        print(f"  - {c}")

    print("\n可用 CIDR:")
    for c in available_cidrs:
        print(f"  - {c}")

    if not available_cidrs:
        print("\n❌ 沒有可用子網，請確認 pool 或 CSV 資料。")
        return


if __name__ == "__main__":
    main()
