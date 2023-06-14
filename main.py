import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ttkthemes import ThemedTk
import bq_table_creator
import gcp_uploader
import file_converter
from google.cloud import bigquery


# GCP Credential
def select_gcp_key(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(tk.END, file_path)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = file_path


# Schema Builder
VALID_TYPES = ["STRING", "BYTES", "INTEGER", "FLOAT", "BOOLEAN", "TIMESTAMP", "DATE", "TIME", "DATETIME", "RECORD"]

class SchemaBuilder:
    def __init__(self, master):
        self.master = master
        self.schema_frame = ttk.Frame(master)
        self.schema_frame.grid(sticky='nsew') # Changed pack to grid

        self.columns = []
        self.add_column()

        self.add_button = ttk.Button(self.schema_frame, text='+', command=self.add_column)
        self.add_button.grid() # Changed pack to grid

    def add_column(self):
        column_frame = ttk.Frame(self.schema_frame)
        column_frame.grid() # Changed pack to grid

        ttk.Label(column_frame, text='Nome da Coluna:').grid(sticky='w') # Changed pack to grid
        name_entry = ttk.Entry(column_frame)
        name_entry.grid() # Changed pack to grid

        ttk.Label(column_frame, text='Tipo de Dados:').grid(sticky='w') # Changed pack to grid
        type_entry = ttk.Entry(column_frame)
        type_entry.grid() # Changed pack to grid

        remove_button = ttk.Button(column_frame, text='-', command=lambda: self.remove_column(column_frame))
        remove_button.grid() # Changed pack to grid

        self.columns.append((column_frame, name_entry, type_entry))

    def remove_column(self, column_frame):
        self.columns = [(frame, name_entry, type_entry) for frame, name_entry, type_entry in self.columns if frame != column_frame]
        column_frame.destroy()

    def get_schema(self):
        schema = []
        for _, name_entry, type_entry in self.columns:
            name = name_entry.get()
            type_ = type_entry.get()
            if name and type_:
                schema.append(bigquery.SchemaField(name, type_))
        return schema

    def validate(self):
        names = [name_entry.get() for _, name_entry, _ in self.columns]
        types = [type_entry.get() for _, _, type_entry in self.columns]

        if "" in names or "" in types:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return False

        if len(set(names)) != len(names):
            messagebox.showerror("Erro", "Os nomes das colunas devem ser únicos.")
            return False

        if any(type_.upper() not in VALID_TYPES for type_ in types):
            messagebox.showerror("Erro", "Tipos de dados inválidos. Por favor, use um dos seguintes: " + ', '.join(VALID_TYPES))
            return False

        return True


# Application features
def browse_files(entry):
    directory = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(tk.END, directory)

def convert_files(input_dir_entry, output_dir_entry, progress):
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()
    if not input_dir or not output_dir:
        messagebox.showerror("Erro", "Por favor, selecione os diretórios de entrada e saída.")
        return
    message = file_converter.convert_files(input_dir, output_dir, progress, root)
    messagebox.showinfo("Informação", message)

def upload_files(bucket_name_entry, source_dir_entry, progress):
    bucket_name = bucket_name_entry.get()
    source_dir = source_dir_entry.get()
    if not bucket_name or not source_dir:
        messagebox.showerror("Erro", "Por favor, preencha o nome do bucket e selecione o diretório de origem.")
        return
    message = gcp_uploader.upload_files(bucket_name, source_dir, progress, root)
    messagebox.showinfo("Informação", message)
    
def create_tables(dataset_id_entry, table_id_entry, bucket_uri_entry, auto_schema_button, schema_builder, progress, root):
    dataset_id = dataset_id_entry.get()
    table_id = table_id_entry.get()
    bucket_uri = bucket_uri_entry.get()
    auto_schema = auto_schema_button.get()

    if not auto_schema and not schema_builder.validate():
        return

    if not dataset_id or not table_id or not bucket_uri:
        messagebox.showerror("Erro", "Por favor, preencha o ID do conjunto de dados, o ID da tabela e o URI do bucket.")
        return
    try:
        if not auto_schema:
            schema = schema_builder.get_schema()
        else:
            schema = None
        message = bq_table_creator.create_table(dataset_id, table_id, bucket_uri, auto_schema, schema)
        progress['value'] = 100
        root.update_idletasks()
        messagebox.showinfo("Informação", message)
    except Exception as e:
        progress['value'] = 0
        root.update_idletasks()
        messagebox.showerror('Erro', f'Erro ao criar a tabela. {str(e)}')


# Interface generator
root = ThemedTk(theme='lumen')
root.title('Ferramenta de Migração de Dados')

tab_control = ttk.Notebook(root)
tab0 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab0, text='Configuração de GCP')
tab_control.add(tab1, text='Converter Arquivos')
tab_control.add(tab2, text='Upload para GCP')
tab_control.add(tab3, text='Criar Tabelas no BigQuery')
tab_control.pack(expand=1, fill='both')

# Tab0
gcp_key_entry = ttk.Entry(tab0)
gcp_key_entry.grid(row=0, column=1)
ttk.Label(tab0, text='Chave GCP:').grid(row=0, column=0)
ttk.Button(tab0, text='Selecionar', command=lambda: select_gcp_key(gcp_key_entry)).grid(row=0, column=2)

# ProgressBar for Tabs
progress = ttk.Progressbar(root, orient = 'horizontal', mode = 'determinate')
progress.pack(pady=10)

# Tab1
input_dir_entry = ttk.Entry(tab1)
input_dir_entry.grid(row=0, column=1)
ttk.Label(tab1, text='Diretório de Entrada:').grid(row=0, column=0)
ttk.Button(tab1, text='Selecionar', command=lambda: browse_files(input_dir_entry)).grid(row=0, column=2)

output_dir_entry = ttk.Entry(tab1)
output_dir_entry.grid(row=1, column=1)
ttk.Label(tab1, text='Diretório de Saída:').grid(row=1, column=0)
ttk.Button(tab1, text='Selecionar', command=lambda: browse_files(output_dir_entry)).grid(row=1, column=2)

ttk.Button(tab1, text='Converter', command=lambda: convert_files(input_dir_entry, output_dir_entry, progress)).grid(row=2, column=1)

# Tab2
bucket_name_entry = ttk.Entry(tab2)
bucket_name_entry.grid(row=0, column=1)
ttk.Label(tab2, text='Nome do Bucket:').grid(row=0, column=0)

source_dir_entry = ttk.Entry(tab2)
source_dir_entry.grid(row=1, column=1)
ttk.Label(tab2, text='Diretório de Origem:').grid(row=1, column=0)
ttk.Button(tab2, text='Selecionar', command=lambda: browse_files(source_dir_entry)).grid(row=1, column=2)

ttk.Button(tab2, text='Upload', command=lambda: upload_files(bucket_name_entry, source_dir_entry, progress)).grid(row=2, column=1)

# Tab3
dataset_id_entry = ttk.Entry(tab3)
dataset_id_entry.grid(row=0, column=1)
ttk.Label(tab3, text='ID do Conjunto de Dados:').grid(row=0, column=0)

table_id_entry = ttk.Entry(tab3)
table_id_entry.grid(row=1, column=1)
ttk.Label(tab3, text='ID da Tabela:').grid(row=1, column=0)

bucket_uri_entry = ttk.Entry(tab3)
bucket_uri_entry.grid(row=2, column=1)
ttk.Label(tab3, text='URI do Bucket:').grid(row=2, column=0)

auto_schema_button = ttk.Checkbutton(tab3, text='Criar Esquema Automaticamente')
auto_schema_button.grid(row=3, column=1)

# Add the Schema Builder frame only in tab3
schema_builder = SchemaBuilder(tab3)

ttk.Button(tab3, text='Criar Tabela', command=lambda: create_tables(dataset_id_entry, table_id_entry, bucket_uri_entry, auto_schema_button, schema_builder, progress, root)).grid(row=4, column=1)

root.mainloop()
