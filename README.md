# App para a gestão de conversão e upload de dados no GCP e criação de tabelas no BigQuery


Desenvolvi uma interface gráfica que permite ao usuário:

- Converter arquivos dos formatos XML,XMLS e SAV para CSV, permitindo assim a consistência do formato dos arquivos e sua posterior utilização em diferentes plataformas;

* Realizar o upload de arquivos CSV para um bucket existente no GCP;

+ Criar uma tabela a partir dos dados de um bucket específico (1 tabela para todos os arquivos do bucket);

A aplicação oferece a possibilidade de realizar essas operações sem a necessidade de alterações no código-fonte, Possui validação dos inputs e necessita que o usuário defina sua chave de acesso IAM em uma variável de ambiente GOOGLE_APPLICATION_CREDENTIALS.

```

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "caminho_para_o_seu_arquivo_de_chave.json"


```

IFSP Caraguatatuba, 5/2023