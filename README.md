以下は現在進行中のデータエンジニアリング学習プロジェクトの状況です。続きを手伝ってください。

## プロジェクト概要
S&P 500・VT・USD/JPYの金融データを毎日自動で収集・整形・可視化するパイプラインを構築中。

## 使用技術スタック
- データ取得：yfinance（Python）
- ストレージ：GCS
- DWH：BigQuery
- 変換：dbt Core
- オーケストレーション：Airflow（Dockerで起動）
- 可視化：Looker Studio
- コード管理：GitHub

## データの流れ
yfinance API → GCS → BigQuery → dbt → Looker Studio
全体をAirflow（Docker）が毎日自動実行

## GitHubリポジトリ
https://github.com/DonguriAcorn/finance-pipeline

## フォルダ構成

```
finance-pipeline/
├── dags/
├── scripts/
│   ├── fetch_finance.py    # yfinance → GCS
│   └── load_to_bigquery.py # GCS → BigQuery
├── notebooks/
│   └── explore.ipynb
├── dbt/
├── docker-compose.yaml
├── .env
├── gcp-key.json
└── README.md
```

## GCP構成
- GCSバケット：finance-pipeline-raw-202606（asia-northeast1）
- BigQueryデータセット：finance_pipeline（asia-northeast1）
- テーブル：sp500_raw・vt_raw・usdjpy_raw
- サービスアカウント：finance-pipeline-sa

## 4週間ロードマップ
- [x] Week 1：環境構築
- [ ] Week 2：Extract → Load ← 今ここ
- [ ] Week 3：Transform（dbt）
- [ ] Week 4：仕上げ

## Week 2の進捗
- [x] uv仮想環境作成
- [x] yfinanceデータ取得スクリプト作成（fetch_finance.py）
- [x] GCSバケット作成・アップロード確認
- [x] BigQueryへのロード確認（load_to_bigquery.py）
- [ ] AirflowのDAGに組み込む ← 次のステップ

## 環境
- Mac（Intel Core i5, 16GB RAM）
- VS Code
- Python 3.13（uv仮想環境）
- Airflow 3.2.2（Docker）起動済み
- GCPプロジェクトID：my-sandbox-498601