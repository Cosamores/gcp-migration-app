from google.cloud import storage
import os

def upload_files(bucket_name, source_dir):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    for filename in os.listdir(source_dir):
        if filename.endswith('.csv'):
            blob = bucket.blob(filename)
            blob.upload_from_filename(os.path.join(source_dir, filename))
    return "Upload de arquivos concluído"
