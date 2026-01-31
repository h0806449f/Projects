import glob
import pandas as pd
import ipaddress

# -----------------------------
# 讀取 CSV
# -----------------------------
# 讀取唯一的 result_*.csv
vpc_files = glob.glob("result_*.csv")
if not vpc_files:
    raise FileNotFoundError("No result_*.csv file found")
vpc_df = pd.read_csv(vpc_files[0])

# 讀取 TGW CSV
tgw_df = pd.read_csv("vpc_transit_gateway_info.csv")

# -----------------------------
# 過濾 TGW 只保留 VPC attachment
# -----------------------------
tgw_vpc_df = tgw_df[tgw_df["TransitGatewayAttachmentType"] == "vpc"].copy()


# 將 ResourceId 改名成 VpcId
tgw_vpc_df = tgw_vpc_df.rename(columns={"ResourceId": "VpcId"})

# 只保留 join 需要的欄位 + Owner
tgw_vpc_df = tgw_vpc_df[["Account", "Region", "VpcId", "TransitGatewayOwnerId"]].drop_duplicates()

# -----------------------------
# FILTER
# network account = 629134176504
tgw_vpc_df["TransitGatewayOwnerId"] = tgw_vpc_df["TransitGatewayOwnerId"].astype(str)
TARGET_OWNER = "629134176504"
tgw_vpc_df = tgw_vpc_df[tgw_vpc_df["TransitGatewayOwnerId"] == TARGET_OWNER]

# AWS region PROD-TGW 才有的 region 
ALLOWED_REGIONS = [
    "ap-east-1",
    "ap-northeast-1",
    "ap-southeast-1",
    "ap-southeast-3",
    "eu-west-2",
    "me-central-1",
    "us-east-1",
    "us-east-2",
]
tgw_vpc_df = tgw_vpc_df[tgw_vpc_df["Region"].isin(ALLOWED_REGIONS)]


# -----------------------------
# merge VPC 與 TGW
# -----------------------------
merged_df = pd.merge(
    vpc_df,
    tgw_vpc_df,
    on=["Account", "Region", "VpcId"],
    how="inner"  # 只保留有 TGW 且 Owner 正確的 VPC
)


# -----------------------------
# 整理成輸出格式
# -----------------------------
merged_df = merged_df[[
    "Region",
    "VpcCidr",
    "AccountName",
    "Account",
    "VpcName"
]].rename(columns={
    "Region": "region",
    "VpcCidr": "vpc_cidr",
    "AccountName": "account_name",
    "Account": "account_id",
    "VpcName": "vpc_name"
})

# -----------------------------
# 拆分多個 CIDR，每個 CIDR 建立一列
# -----------------------------
vpc_rows = []

for _, row in merged_df.iterrows():
    # 拆分多個 CIDR，去除空格
    for cidr in row['vpc_cidr'].split(','):
        cidr = cidr.strip()
        if cidr:  # 避免空字串
            try:
                # 驗證 CIDR 是否正確
                net = ipaddress.IPv4Network(cidr)
                vpc_rows.append({
                    "region": row['region'],
                    "vpc_cidr": cidr,
                    "account_name": row['account_name'],
                    "account_id": row['account_id'],
                    "vpc_name": row['vpc_name'],
                    "network_int": int(net.network_address)  # 使用整數作為排序輔助
                })
            except ValueError:
                print(f"跳過無效 CIDR: {cidr}")

# 建立新的 DataFrame
result_df_expanded = pd.DataFrame(vpc_rows)

# 檢查是否有資料
if not result_df_expanded.empty:
    # 依 IP 整數排序
    result_df_expanded = result_df_expanded.sort_values(by="network_int").reset_index(drop=True)
    # 排序完成後刪掉輔助欄位
    result_df_expanded = result_df_expanded.drop(columns=["network_int"])

# 顯示結果
print(result_df_expanded)

# 可選：寫出 CSV
result_df_expanded.to_csv("1_output_vpc_with_prod_tgw.csv", index=False)