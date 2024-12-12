from prefect import flow
from prefect_dbt.cloud import DbtCloudCredentials, DbtCloudJob
from prefect_dbt.cloud.jobs import run_dbt_cloud_job


@flow
def flow_dbt():
    dbt_cloud_credentials = DbtCloudCredentials.load("NESTLE snowflake")
    dbt_cloud_job = DbtCloudJob(
        dbt_cloud_credentials=dbt_cloud_credentials, job_id=776963
    )
    return run_dbt_cloud_job(dbt_cloud_job=dbt_cloud_job)
