from prefect import flow, task
from azure.storage.blob import BlobServiceClient
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import json
import os
import time
from sap_tables import SAP_TABLES
from prefect.variables import Variable

# Azure Configuration
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=bysapingestion;AccountKey=6aYk64jd0qnGOSjI0akLLmA3T6upacsNywRhqCtg8LsfFmZtDJwkpctHN64d5QbrBkOp1Y9UA/0h+ASt0lLMxA==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "ingestionfiles"


@task
def fetch_paginated_data(
    api_url: str, username: str, password: str, skip: int, top: int = 10000
) -> list:
    # """
    # Fetch a single page of data from the OData API.
    # """
    session = requests.Session()
    session.cookies.clear()

    paginated_url = f"{api_url}&$top={top}&$skip={skip}"
    print(paginated_url)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = session.get(
        paginated_url, auth=HTTPBasicAuth(username, password), headers=headers
    )
    response.raise_for_status()

    data = response.json()
    results = data.get("d", {}).get("results", [])
    return results


@task
def save_to_file(data: list, file_path: str):
    """
    Save data to a file, appending if the file already exists.
    """
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            existing_data = json.load(f)
        data = existing_data + data

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {file_path}")


@task
def upload_to_azure(file_path: str, blob_name: str):
    blob_service_client = BlobServiceClient.from_connection_string(
        AZURE_CONNECTION_STRING
    )
    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME, blob=blob_name
    )

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"{blob_name} uploaded successfully to Azure Blob Storage.")


@flow(retries=0, retry_delay_seconds=5, log_prints=True)
def sap_ingestion_flow():
    file_path = "api_response.json"
    for table in SAP_TABLES:
        skip = 0
        top = 1000
        has_more_data = True

        # data = fetch_paginated_data(
        #     table["url"], "STUDENT006", "Hakkoda2025", skip, top
        # )
        # save_to_file(data, file_path)
        while has_more_data:
            data = fetch_paginated_data(
                table["url"], "STUDENT006", "Hakkoda2025", skip, top
            )

            if not data:
                has_more_data = False
            else:
                save_to_file(data, file_path)
                skip += top

        if os.path.exists(file_path):
            upload_to_azure(file_path, table["blob_name"])

        os.remove(file_path)


if __name__ == "__main__":
    sap_ingestion_flow.serve(
        name="sap-ingestion",
        tags=["onboarding"],
    )
