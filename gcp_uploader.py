from google.cloud import storage
import os
import logging

def upload_files(bucket_name, source_dir, progress, root):
    logging.info('Iniciando o upload de arquivos')
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    for idx, filename in enumerate(os.listdir(source_dir)):
        if filename.endswith('.csv'):
            blob = bucket.blob(filename)
            blob.upload_from_filename(os.path.join(source_dir, filename))
            progress['value'] = (idx+1)/len(os.listdir(source_dir))*100
            root.update_idletasks()
    logging.info('Upload de arquivos concluído')
    return "Upload de arquivos concluído"
