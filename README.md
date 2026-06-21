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
│   └── finance_pipeline.py    # AirflowのDAG
├── scripts/
│   ├── fetch_finance.py       # yfinance → GCS
│   └── load_to_bigquery.py    # GCS → BigQuery
├── notebooks/
│   └── explore.ipynb
├── dbt/
│   └── finance_dbt/           # dbtプロジェクト
│       ├── dbt_project.yml
│       ├── models/
│       ├── macros/
│       └── seeds/
├── docker-compose.yaml
├── .env                       # ローカルのみ
├── gcp-key.json               # ローカルのみ
└── README.md
```

## GCP構成
- GCSバケット：finance-pipeline-raw-202606（asia-northeast1）
- BigQueryデータセット：
  - finance_pipeline（rawデータ）
  - finance_staging（stagingモデル出力先）
  - finance_marts（martsモデル出力先）
- テーブル：sp500_raw・vt_raw・usdjpy_raw
- サービスアカウント：finance-pipeline-sa
- GCPプロジェクトID：my-sandbox-498601

## 4週間ロードマップ
- [x] Week 1：環境構築
- [x] Week 2：Extract → Load
- [ ] Week 3：Transform（dbt） ← 今ここ
- [ ] Week 4：仕上げ

## Week 2の進捗
- [x] uv仮想環境作成
- [x] yfinanceデータ取得スクリプト作成（fetch_finance.py）
- [x] GCSバケット作成・アップロード確認
- [x] BigQueryへのロード確認（load_to_bigquery.py）
- [x] AirflowのDAGに組み込む（finance_pipeline.py）

## Week 3の進捗
- [x] dbt-bigqueryインストール
- [x] dbtプロジェクト作成（finance_dbt）
- [x] BigQuery接続確認（dbt debug）
- [x] dbt_project.yml設定（staging/marts層の分離）
- [ ] sourcesの定義
- [ ] stagingモデルの作成
- [ ] martsモデルの作成
- [ ] テスト・ドキュメントの作成

## 環境
- Mac（Intel Core i5, 16GB RAM）
- VS Code
- Python 3.13（uv仮想環境）
- Airflow 3.2.2（Docker）
- dbt-fusion 2.0.0-preview.186
- GCPプロジェクトID：my-sandbox-498601