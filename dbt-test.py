from prefect import flow
from prefect_dbt.cloud import DbtCloudCredentials, DbtCloudJob
from prefect_dbt.cloud.jobs import run_dbt_cloud_job


@flow
def run_dbt_cloud_job_flow(dbt_job_id, dbt_creds):
    dbt_cloud_credentials = DbtCloudCredentials.load(dbt_creds)
    dbt_cloud_job = DbtCloudJob(
        dbt_cloud_credentials=dbt_cloud_credentials, job_id=dbt_job_id
    )
    return run_dbt_cloud_job(dbt_cloud_job=dbt_cloud_job)
