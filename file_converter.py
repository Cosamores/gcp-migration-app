import os
import pandas as pd
import pyreadstat

def convert_files(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(input_dir, filename))
            df.to_csv(os.path.join(output_dir, filename.replace('.xlsx', '.csv')), index=False)
        elif filename.endswith('.sav'):
            df, meta = pyreadstat.read_sav(os.path.join(input_dir, filename))
            df.to_csv(os.path.join(output_dir, filename.replace('.sav', '.csv')), index=False)
    return "Conversão de arquivos concluída"
