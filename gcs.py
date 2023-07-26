import requests
from google.cloud import storage

path_to_private_key = './cred.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)
bucket = storage.Bucket(client, 'bulk_uploadtest')

list_files_to_upload = [
    'https://filemanager.gupshup.io/fm/wamedia/ColoredCow/1099e8e4-83e9-4169-b260-ceb394d6574f',
    'https://filemanager.gupshup.io/fm/wamedia/ColoredCow/69edddc3-cd52-453a-af66-f2d3e0959d8a'
]

for url in list_files_to_upload:
    response = requests.get(url)
    if response.status_code == 200:
        file_content = response.content
        # Extract the file name from the URL
        file_name = url.split("/")[-1]
        # Upload the file content to GCS
        blob = bucket.blob(file_name)
        blob.upload_from_string(file_content)
        print(f"File {file_name} uploaded successfully to GCS.")
    else:
        print(f"Failed to fetch the content from URL: {url}")
