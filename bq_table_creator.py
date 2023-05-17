from google.cloud import bigquery

def create_tables(dataset_id, table_id, schema):
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)
    return "Criação de tabelas concluída"
