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

## 進捗
- [x] GitHubリポジトリ作成
- [x] フォルダ構成作成
- [ ] Docker ComposeでAirflow立ち上げ
- [ ] GCSバケット・BigQueryデータセット作成
- [ ] Hello WorldのDAG作成
- [ ] yfinanceデータ取得・GCS/BigQueryへのロード
- [ ] dbtモデル作成
- [ ] Looker Studio可視化