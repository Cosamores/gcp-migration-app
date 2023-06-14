from google.cloud import bigquery
import logging

def create_table(dataset_id, table_id, bucket_uri, auto_schema=True, schema=None):
    """Create a BigQuery table and load data from a GCP Bucket.

    Args:
        dataset_id (str): ID of the BigQuery dataset.
        table_id (str): ID of the BigQuery table.
        bucket_uri (str): GCP Bucket URI of the file to load.
        auto_schema (bool): Whether to automatically infer the schema.
        schema (list[google.cloud.bigquery.schema.SchemaField], optional): The schema of the table. Ignored if auto_schema is True.
    """
    logging.info('Iniciando a criação da tabela')
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.autodetect = auto_schema
    if not auto_schema and schema is not None:
        job_config.schema = schema

    load_job = client.load_table_from_uri(bucket_uri, table_ref, job_config=job_config)
    load_job.result()
    logging.info('Criação de tabelas concluída')
    return "Criação de tabelas concluída"
