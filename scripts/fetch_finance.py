import yfinance as yf
import pandas as pd
from google.cloud import storage
from datetime import datetime, timedelta
import os
import sys

# 設定
BUCKET_NAME = "finance-pipeline-raw-202606"
GCP_KEY_PATH = os.path.join(os.path.dirname(__file__), "../gcp-key.json")
TICKERS = {
    "sp500": "^GSPC",
    "vt": "VT",
    "usdjpy": "JPY=X"
}

def fetch_and_upload(execution_date: str = None):
    # execution_dateが指定されていれば使う、なければ今日
    if execution_date:
        target_date = datetime.strptime(execution_date, "%Y-%m-%d")
    else:
        target_date = datetime.today()

    today = target_date.strftime("%Y-%m-%d")
    start = (target_date - timedelta(days=5)).strftime("%Y-%m-%d")

    # GCSクライアント初期化
    storage_client = storage.Client.from_service_account_json(GCP_KEY_PATH)
    bucket = storage_client.bucket(BUCKET_NAME)

    for name, ticker in TICKERS.items():
        df = yf.download(ticker, start=start, end=today)
        df.columns = df.columns.get_level_values(0)
        df.reset_index(inplace=True)

        csv_data = df.to_csv(index=False)

        blob_path = f"{name}/{today}.csv"
        blob = bucket.blob(blob_path)
        blob.upload_from_string(csv_data, content_type="text/csv")
        print(f"Uploaded: {blob_path}")

if __name__ == "__main__":
    # コマンドライン引数で日付を受け取る
    execution_date = sys.argv[1] if len(sys.argv) > 1 else None
    fetch_and_upload(execution_date)