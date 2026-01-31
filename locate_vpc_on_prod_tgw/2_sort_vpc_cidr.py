import pandas as pd
import ipaddress

# -----------------------------
# 讀入整理好的 VPC CSV
# -----------------------------
vpc_df = pd.read_csv("1_output_vpc_with_prod_tgw.csv")

# -----------------------------
# 拆分多個 CIDR 並轉成 ipaddress 物件
# -----------------------------
vpc_rows = []

for _, row in vpc_df.iterrows():
    for cidr in row['vpc_cidr'].split(','):
        cidr = cidr.strip()
        if cidr:
            try:
                net = ipaddress.IPv4Network(cidr)
                vpc_rows.append({
                    "network": net,
                    "vpc_cidr": cidr,
                    "region": row['region'],
                    "account_name": row['account_name'],
                    "account_id": row['account_id'],
                    "vpc_name": row['vpc_name']
                })
            except ValueError:
                print(f"跳過無效 CIDR: {cidr}")

vpc_df_expanded = pd.DataFrame(vpc_rows)

# -----------------------------
# 定義 /8 pool
# -----------------------------
pool = ipaddress.IPv4Network("10.0.0.0/8")

# -----------------------------
# 建立 /16 分析表
# -----------------------------
rows = []

for sub16 in pool.subnets(new_prefix=16):
    used_vpcs = vpc_df_expanded[
        vpc_df_expanded['network'].apply(lambda x: x.overlaps(sub16))
    ]

    if not used_vpcs.empty:
        # 依 VPC CIDR 的實際網路位址排序
        used_vpcs = used_vpcs.sort_values(by="network")

        for _, v in used_vpcs.iterrows():
            rows.append({
                "CIDR/16": str(sub16),
                "using": True,
                "vpc_cidr": v['vpc_cidr'],
                "region": v['region'],
                "account_name": v['account_name'],
                "account_id": v['account_id'],
                "vpc_name": v['vpc_name']
            })
    else:
        rows.append({
            "CIDR/16": str(sub16),
            "using": False,
            "vpc_cidr": "",
            "region": "",
            "account_name": "",
            "account_id": "",
            "vpc_name": ""
        })

# -----------------------------
# 轉成 DataFrame
# -----------------------------
ipam_df = pd.DataFrame(rows)

# -----------------------------
# ⭐ 正確排序（關鍵修正）
# -----------------------------
# 新增一個用來排序的 IPv4Network 欄位
ipam_df["cidr_net"] = ipam_df["CIDR/16"].apply(ipaddress.IPv4Network)

# 用數值順序排序，而不是字串
ipam_df = (
    ipam_df
    .sort_values(by=["cidr_net", "vpc_cidr"])
    .drop(columns=["cidr_net"])
    .reset_index(drop=True)
)

# -----------------------------
# 輸出 CSV
# -----------------------------
ipam_df.to_csv("prod_tgw_prefix_16.csv", index=False)

# 顯示前 20 筆
print(ipam_df.head(20))
