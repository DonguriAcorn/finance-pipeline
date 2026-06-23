from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="finance_pipeline",
    default_args=default_args,
    description="Fetch finance data and load to BigQuery",
    schedule="0 9 * * 1-5",  # 平日9時に実行
    start_date=datetime(2026, 6, 1),
    catchup=False,
    tags=["finance"],
) as dag:

    fetch = BashOperator(
        task_id="fetch_finance",
        bash_command="cd /opt/airflow && python scripts/fetch_finance.py",
    )

    load = BashOperator(
        task_id="load_to_bigquery",
        bash_command="cd /opt/airflow && python scripts/load_to_bigquery.py",
    )
    
    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/dbt/finance_dbt && dbt run --profiles-dir /opt/airflow/dbt/finance_dbt",
    )

    
    dbt_test = BashOperator(
        task_id="dbt_test",
    bash_command="cd /opt/airflow/dbt/finance_dbt && dbt test --profiles-dir /opt/airflow/dbt/finance_dbt",
    )
    
    fetch >> load >> dbt_run >> dbt_test
