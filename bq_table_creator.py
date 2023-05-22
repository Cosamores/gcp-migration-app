from google.cloud import bigquery
import logging

def create_tables(dataset_id, table_id, schema, progress, root):
    logging.info('Iniciando a criação de tabelas')
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)
    progress['value'] = 100
    root.update_idletasks()
    logging.info('Criação de tabelas concluída')
    return "Criação de tabelas concluída"
