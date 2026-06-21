以下は現在進行中のデータエンジニアリング学習プロジェクトの状況です。続きを手伝ってください。

## プロジェクト概要
S&P 500・VT・USD/JPYの金融データを毎日自動で収集・整形・可視化するパイプラインを構築中。

## 使用技術スタック
- データ取得：yfinance（Python）
- ストレージ：GCS
- DWH：BigQuery
- 変換：dbt Core（dbt-fusion 2.0.0）
- オーケストレーション：Airflow 3.2.2（Dockerで起動）
- 可視化：Looker Studio
- コード管理：GitHub

## データの流れ
```
yfinance API
　　↓ fetch_finance.py
GCS（finance-pipeline-raw-202606）
　　↓ load_to_bigquery.py
BigQuery（finance_pipeline）
　　sp500_raw / vt_raw / usdjpy_raw
　　↓ dbt
finance_pipeline_staging
　　stg_sp500 / stg_vt / stg_usdjpy（view）
　　↓
finance_pipeline_marts
　　mart_finance（table）
　　↓
Looker Studio（Week 4）
全体をAirflow（Docker）が毎日自動実行
```

## GitHubリポジトリ
https://github.com/DonguriAcorn/finance-pipeline

## フォルダ構成
```
finance-pipeline/
├── dags/
│   └── finance_pipeline.py       # AirflowのDAG
├── scripts/
│   ├── fetch_finance.py          # yfinance → GCS
│   └── load_to_bigquery.py       # GCS → BigQuery
├── notebooks/
│   └── explore.ipynb
├── dbt/
│   └── finance_dbt/
│       ├── dbt_project.yml
│       ├── models/
│       │   ├── sources.yml
│       │   ├── staging/
│       │   │   ├── stg_sp500.sql
│       │   │   ├── stg_vt.sql
│       │   │   ├── stg_usdjpy.sql
│       │   │   └── schema.yml
│       │   └── marts/
│       │       └── mart_finance.sql
│       ├── macros/
│       └── seeds/
├── docker-compose.yaml
├── .env                          # ローカルのみ・GitHubに上げない
├── gcp-key.json                  # ローカルのみ・GitHubに上げない
└── README.md
```

## GCP構成
- GCPプロジェクトID：my-sandbox-498601
- GCSバケット：finance-pipeline-raw-202606（asia-northeast1）
- BigQueryデータセット：
  - finance_pipeline（rawデータ）
  - finance_pipeline_staging（stagingモデル出力先）
  - finance_pipeline_marts（martsモデル出力先）
- 生テーブル：sp500_raw・vt_raw・usdjpy_raw
- サービスアカウント：finance-pipeline-sa
- 認証キー：gcp-key.json（ローカルのみ）

## 環境
- Mac（Intel Core i5, 16GB RAM）
- VS Code
- Python 3.13（uv仮想環境）
- Airflow 3.2.2（Docker・LocalExecutor）
- dbt-fusion 2.0.0-preview.186
- profiles.yml：~/.dbt/profiles.yml（finance_dbtプロファイル）

## 4週間ロードマップ
- [x] Week 1：環境構築
- [x] Week 2：Extract → Load
- [x] Week 3：Transform（dbt）
- [ ] Week 4：仕上げ ← 次はここ

## Week 3の完了内容
- [x] dbt-bigqueryインストール
- [x] dbtプロジェクト作成（finance_dbt）
- [x] BigQuery接続確認（dbt debug）
- [x] dbt_project.yml設定（staging/marts層の分離）
- [x] sources.yml定義
- [x] stagingモデル作成（重複除去・カラム名統一）
- [x] martsモデル作成（mart_finance）
- [x] テスト作成・全テスト通過（7/7）

## Week 4でやること
- [ ] dbt docsでドキュメント生成
- [ ] Looker StudioでBigQueryのデータを可視化
- [ ] AirflowのDAGにdbt runを組み込む
- [ ] README整備・ポートフォリオとして仕上げる

## 起動方法
```bash
# 仮想環境の有効化
source .venv/bin/activate

# Airflow起動
docker compose up -d

# データ取得・ロード
python scripts/fetch_finance.py
python scripts/load_to_bigquery.py

# dbt実行
cd dbt/finance_dbt
uv run dbt run
uv run dbt test
```