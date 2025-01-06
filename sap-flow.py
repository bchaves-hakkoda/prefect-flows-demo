from prefect import flow, task
from azure.storage.blob import BlobServiceClient
import requests
import json
import os

# Azure Configuration
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=bysapingestion;AccountKey=6aYk64jd0qnGOSjI0akLLmA3T6upacsNywRhqCtg8LsfFmZtDJwkpctHN64d5QbrBkOp1Y9UA/0h+ASt0lLMxA==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "ingestionfiles"
BLOB_NAME = "api_response.json"

# API Endpoint
API_URL = "https://sapingest.free.beeceptor.com/table1"


@task
def call_api(api_url: str) -> dict:
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()


@task
def save_to_file(data: dict, file_path: str):
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


@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    file_path = "api_response.json"

    # Call API and save to file
    data = call_api(API_URL)
    save_to_file(data, file_path)

    # Upload to Azure
    upload_to_azure(file_path, BLOB_NAME)

    # Cleanup
    os.remove(file_path)

    if goodbye:
        print(f"Goodbye {name}!")


if __name__ == "__main__":
    hello_world.serve(
        name="my-first-deployment",
        tags=["onboarding"],
        parameters={"goodbye": True},
        interval=60,
    )
