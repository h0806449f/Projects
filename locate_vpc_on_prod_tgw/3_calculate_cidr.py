import pandas as pd
import ipaddress

INPUT_FILE = "prod_tgw_prefix_16.csv"
OUTPUT_FILE = "prod_tgw_prefix_within_16.csv"

# --------------------------------------------------
# 1. 讀取資料，只處理 using == TRUE
# --------------------------------------------------
df = pd.read_csv(INPUT_FILE)
df["using"] = df["using"].astype(str).str.upper() == "TRUE"

used_df = df[df["using"]]

# --------------------------------------------------
# 2. 將 vpc_cidr 轉成 ipaddress 物件
# --------------------------------------------------
used_networks = {}

for _, row in used_df.iterrows():
    cidr_16 = row["CIDR/16"]
    vpc_cidr = row["vpc_cidr"]

    if not vpc_cidr or pd.isna(vpc_cidr):
        continue

    try:
        net16 = ipaddress.ip_network(cidr_16)
        vpc_net = ipaddress.ip_network(vpc_cidr)
    except ValueError:
        continue

    used_networks.setdefault(net16, []).append(vpc_net)

# --------------------------------------------------
# 3. 計算 available CIDR (/17 ~ /22)
# --------------------------------------------------
rows = []

for net16, vpc_nets in used_networks.items():
    for prefix in range(17, 23):
        available = []

        for subnet in net16.subnets(new_prefix=prefix):
            if any(subnet.overlaps(v) for v in vpc_nets):
                continue
            available.append(subnet)

        rows.append({
            "CIDR/16": str(net16),
            "prefix": f"/{prefix}",
            "available_count": len(available),
            "available_cidrs": ", ".join(str(n) for n in available)
        })

# --------------------------------------------------
# 4. 建立 DataFrame
# --------------------------------------------------
available_df = pd.DataFrame(rows)

# --------------------------------------------------
# 5. 正確排序（IP 數值排序 + prefix 數值排序）
# --------------------------------------------------
available_df = available_df.sort_values(
    by=["CIDR/16", "prefix"],
    key=lambda col: (
        col.map(lambda x: ipaddress.ip_network(x).network_address)
        if col.name == "CIDR/16"
        else col.str.replace("/", "").astype(int)
    )
)

# --------------------------------------------------
# 6. 去除沒有可用 CIDR 的資料 optional
# --------------------------------------------------
# available_df = available_df[available_df["available_count"] > 0]

# --------------------------------------------------
# 7. 在不同 CIDR/16 之間插入空白行
# --------------------------------------------------
rows = []
prev_cidr16 = None

for _, row in available_df.iterrows():
    current_cidr16 = row["CIDR/16"]

    # 如果 CIDR/16 改變，插入一行空白
    if prev_cidr16 is not None and current_cidr16 != prev_cidr16:
        rows.append({
            "CIDR/16": "",
            "prefix": "",
            "available_count": "",
            "available_cidrs": ""
        })

    rows.append(row.to_dict())
    prev_cidr16 = current_cidr16

available_df = pd.DataFrame(rows)

# --------------------------------------------------
# 8. 輸出結果
# --------------------------------------------------
available_df.to_csv(OUTPUT_FILE, index=False)

print("完成！輸出檔案：", OUTPUT_FILE)
print(available_df.head(20))
