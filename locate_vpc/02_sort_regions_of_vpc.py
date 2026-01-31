import pandas as pd
import os
import logging

# 設置日誌
logging.basicConfig(
    filename='vpc_check.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def aggregate_df(summary_file: str = "RAWDATA_vpc_summary.csv"):
    if not os.path.exists(summary_file):
        logging.warning("Summary file does not exist. Skip aggregation.")
        print("Summary file does not exist. Skip aggregation.")
        return

    df = pd.read_csv(summary_file)
    result = df.groupby("Account")["Region"].agg(lambda x: ", ".join(sorted(set(x)))).reset_index()
    result.columns = ["Account", "Activate_Region"]
    result.to_csv("00_account_region_mapping.csv", index=False)
    logging.info("✅ Aggregation completed, output written to account_region_mapping.csv")
    print("✅ Aggregation completed, output written to account_region_mapping.csv")

if __name__ == "__main__":
    aggregate_df()