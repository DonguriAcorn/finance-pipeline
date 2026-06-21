from google.cloud import bigquery
from datetime import datetime
import os

GCP_KEY_PATH = os.path.join(os.path.dirname(__file__), "../gcp-key.json")
BUCKET_NAME = "finance-pipeline-raw-202606"
DATASET_ID = "finance_pipeline"
PROJECT_ID = "my-sandbox-498601"

TICKERS = {
    "sp500": "^GSPC",
    "vt": "VT",
    "usdjpy": "JPY=X"
}

def load_to_bigquery():
    client = bigquery.Client.from_service_account_json(GCP_KEY_PATH)
    today = datetime.today().strftime("%Y-%m-%d")

    for name in TICKERS.keys():
        uri = f"gs://{BUCKET_NAME}/{name}/{today}.csv"
        table_id = f"{PROJECT_ID}.{DATASET_ID}.{name}_raw"

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=True,
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,

        )

        load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
        load_job.result()
        print(f"Loaded: {table_id}")

if __name__ == "__main__":
    load_to_bigquery()