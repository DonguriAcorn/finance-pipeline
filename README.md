# finance-pipeline

## 概要
S&P 500・VT・USD/JPYの金融データを毎日自動で収集・整形・可視化するデータパイプライン。

## 技術スタック
- データ取得：yfinance（Python）
- ストレージ：GCS
- DWH：BigQuery
- 変換：dbt Core
- オーケストレーション：Airflow（Docker）
- 可視化：Looker Studio
- コード管理：GitHub

## データの流れ
yfinance API → GCS → BigQuery → dbt → Looker Studio
全体をAirflow（Docker）が毎日自動実行

## 環境
- Mac（Intel Core i5, 16GB RAM）
- VS Code
- Python仮想環境：uv
- Airflow 3.2.2（Docker）

## GCP構成
- プロジェクト：自身のGCPプロジェクト
- GCSバケット：finance-pipeline-raw（asia-northeast1）
- BigQueryデータセット：finance_pipeline（asia-northeast1）
- サービスアカウント：finance-pipeline-sa
- 認証キー：gcp-key.json（ローカルのみ・GitHubには上げない）

## フォルダ構成
finance-pipeline/
├── dags/          # AirflowのDAGファイル
├── scripts/       # Pythonスクリプト（データ取得など）
├── dbt/           # dbtプロジェクト
├── docker-compose.yaml
├── .env
├── gcp-key.json   # ローカルのみ
└── README.md

## 4週間ロードマップ
- [x] Week 1：環境構築（Airflow/Docker/GCS/BigQuery）
- [ ] Week 2：Extract → Load（yfinance → GCS → BigQuery）
- [ ] Week 3：Transform（dbt）
- [ ] Week 4：仕上げ（Looker Studio可視化・README整備）

## Week 2の進捗
- [x] uv仮想環境作成
- [x] GCSバケット作成（finance-pipeline-raw）
- [x] BigQueryデータセット作成（finance_pipeline）
- [x] サービスアカウント・認証キー作成
- [ ] yfinanceデータ取得スクリプト作成
- [ ] GCSへの保存
- [ ] BigQueryへのロード
- [ ] AirflowのDAGに組み込む

---

※ 以下はチャット引き継ぎ用メモ

このREADMEが現在の進捗です。
次のステップは「yfinanceでS&P 500・VT・USD/JPYのデータを取得してGCSに保存するスクリプトをscripts/に作成する」です。