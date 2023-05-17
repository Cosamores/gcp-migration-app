import tkinter as tk
from tkinter import filedialog, messagebox
import bq_table_creator
import gcp_uploader
import file_converter

def browse_files(entry):
    directory = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(tk.END, directory)

def convert_files(input_dir_entry, output_dir_entry):
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()
    if not input_dir or not output_dir:
        messagebox.showerror("Erro", "Por favor, selecione os diretórios de entrada e saída.")
        return
    message = file_converter.convert_files(input_dir, output_dir)
    messagebox.showinfo("Informação", message)

def upload_files(bucket_name_entry, source_dir_entry):
    bucket_name = bucket_name_entry.get()
    source_dir = source_dir_entry.get()
    if not bucket_name or not source_dir:
        messagebox.showerror("Erro", "Por favor, preencha o nome do bucket e selecione o diretório de origem.")
        return
    message = gcp_uploader.upload_files(bucket_name, source_dir)
    messagebox.showinfo("Informação", message)

def create_tables(dataset_id_entry, table_id_entry):
    dataset_id = dataset_id_entry.get()
    table_id = table_id_entry.get()
    if not dataset_id or not table_id:
        messagebox.showerror("Erro", "Por favor, preencha o ID do conjunto de dados e o ID da tabela.")
        return
    message = bq_table_creator.create_tables(dataset_id, table_id, schema=None)
    messagebox.showinfo("Informação", message)

# Continue com a construção da interface gráfica do usuário...

root = tk.Tk()
style = Style('lumen')
root.style = style

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Converter Arquivos')
tab_control.add(tab2, text='Upload para GCP')
tab_control.add(tab3, text='Criar Tabelas no BigQuery')
tab_control.pack(expand=1, fill='both')

# Tab1
input_dir_entry = ttk.Entry(tab1)
input_dir_entry.grid(row=0, column=1)
ttk.Label(tab1, text='Diretório de Entrada:').grid(row=0, column=0)
ttk.Button(tab1, text='Selecionar', command=lambda: select_directory(input_dir_entry)).grid(row=0, column=2)

output_dir_entry = ttk.Entry(tab1)
output_dir_entry.grid(row=1, column=1)
ttk.Label(tab1, text='Diretório de Saída:').grid(row=1, column=0)
ttk.Button(tab1, text='Selecionar', command=lambda: select_directory(output_dir_entry)).grid(row=1, column=2)

ttk.Button(tab1, text='Converter', command=lambda: convert_files(input_dir_entry, output_dir_entry)).grid(row=2, column=1)

# Tab2
bucket_name_entry = ttk.Entry(tab2)
bucket_name_entry.grid(row=0, column=1)
ttk.Label(tab2, text='Nome do Bucket:').grid(row=0, column=0)

source_dir_entry = ttk.Entry(tab2)
source_dir_entry.grid(row=1, column=1)
ttk.Label(tab2, text='Diretório de Origem:').grid(row=1, column=0)
ttk.Button(tab2, text='Selecionar', command=lambda: select_directory(source_dir_entry)).grid(row=1, column=2)

ttk.Button(tab2, text='Upload', command=lambda: upload_files(bucket_name_entry, source_dir_entry)).grid(row=2, column=1)

# Tab3
dataset_id_entry = ttk.Entry(tab3)
dataset_id_entry.grid(row=0, column=1)
ttk.Label(tab3, text='ID do Conjunto de Dados:').grid(row=0, column=0)

table_id_entry = ttk.Entry(tab3)
table_id_entry.grid(row=1, column=1)
ttk.Label(tab3, text='ID da Tabela:').grid(row=1, column=0)

schema_entry = ttk.Entry(tab3)
schema_entry.grid(row=2, column=1)
ttk.Label(tab3, text='Schema:').grid(row=2, column=0)

ttk.Button(tab3, text='Criar', command=lambda: create_tables(dataset_id_entry, table_id_entry, schema_entry)).grid(row=3, column=1)

root.mainloop()
