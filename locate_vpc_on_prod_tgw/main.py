import os
import glob
import subprocess
import sys

# 1. 檢查檔案
result_files = glob.glob("result*.csv")
vpc_file = "vpc_transit_gateway_info.csv"

if not result_files:
    print("Error: 沒有找到以 'result' 開頭的 CSV 檔案")
    sys.exit(1)

if not os.path.isfile(vpc_file):
    print(f"Error: 沒有找到檔案 {vpc_file}")
    sys.exit(1)

print("所有必要檔案存在，開始依序執行腳本...")

# 2. 定義要依序執行的腳本
scripts = ["1_sort_csv.py", "2_sort_vpc_cidr.py", "3_calculate_cidr.py"]

for script in scripts:
    if os.path.isfile(script):
        print(f"執行 {script}...")
        result = subprocess.run(["python3", script])
        if result.returncode != 0:
            print(f"Error: {script} 執行失敗")
            sys.exit(1)
    else:
        print(f"Error: 找不到 {script}")
        sys.exit(1)

print("所有腳本執行完成！")

# 3. 刪除暫存 CSV
temp_files = [
    "1_output_vpc_with_prod_tgw.csv",
    # "2_output_normalize_cidr.csv"
]

for temp_file in temp_files:
    if os.path.isfile(temp_file):
        os.remove(temp_file)
        print(f"已刪除暫存檔案: {temp_file}")
    else:
        print(f"暫存檔案不存在，跳過: {temp_file}")

print("清理完成！")
