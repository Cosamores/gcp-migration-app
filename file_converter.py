import os
import pandas as pd
import pyreadstat
import logging

def convert_files(input_dir, output_dir, progress, root):
    logging.info('Iniciando a conversão dos arquivos')
    for idx, filename in enumerate(os.listdir(input_dir)):
        if filename.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(input_dir, filename))
            df.to_csv(os.path.join(output_dir, filename.replace('.xlsx', '.csv')), index=False)
        elif filename.endswith('.sav'):
            df, meta = pyreadstat.read_sav(os.path.join(input_dir, filename))
            df.to_csv(os.path.join(output_dir, filename.replace('.sav', '.csv')), index=False)
        progress['value'] = (idx+1)/len(os.listdir(input_dir))*100
        root.update_idletasks()
    logging.info('Conversão dos arquivos finalizada')
    return "Conversão de arquivos concluída"
