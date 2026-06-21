import yfinance as yf
import pandas as pd
from google.cloud import storage
from datetime import datetime, timedelta
import os
import json

# 設定
BUCKET_NAME = "finance-pipeline-raw-202606"
GCP_KEY_PATH = os.path.join(os.path.dirname(__file__), "../gcp-key.json")
TICKERS = {
    "sp500": "^GSPC",
    "vt": "VT",
    "usdjpy": "JPY=X"
}

def fetch_and_upload():
    # 昨日の日付を取得
    today = datetime.today().strftime("%Y-%m-%d")
    start = (datetime.today() - timedelta(days=5)).strftime("%Y-%m-%d")

    # GCSクライアント初期化
    storage_client = storage.Client.from_service_account_json(GCP_KEY_PATH)
    bucket = storage_client.bucket(BUCKET_NAME)

    for name, ticker in TICKERS.items():
        # データ取得
        df = yf.download(ticker, start=start, end=today)
        df.columns = df.columns.get_level_values(0)  # 追加
        df.reset_index(inplace=True)

        # CSV化
        csv_data = df.to_csv(index=False)

        # GCSにアップロード
        blob_path = f"{name}/{today}.csv"
        blob = bucket.blob(blob_path)
        blob.upload_from_string(csv_data, content_type="text/csv")
        print(f"Uploaded: {blob_path}")

if __name__ == "__main__":
    fetch_and_upload()