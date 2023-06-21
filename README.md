# Ferramenta de migração de dados para o BigQuery - Documentação de uso

## Sumário

Visão Geral
Instalação e configuração Inicial
Conversão de Arquivos Locais
Upload de Arquivos para o GCP
Criação de Tabelas no BigQuery
Interface Gráfica do Usuário


## Visão Geral
A documentação a seguir descreve o processo de migração de dados que a TAnalytics está utilizando para otimizar o gerenciamento de dados, reduzir custos e melhorar a eficiência. Este processo envolve a conversão de arquivos .xlsx e .sav para .csv, a transferência de arquivos para o Google Cloud Platform (GCP), e a criação de tabelas no BigQuery a partir desses arquivos.

A Ferramenta de Migração de Dados é um aplicativo de desktop projetado para simplificar a migração de dados do sistema local para o Google Cloud Platform, especificamente para o BigQuery.

---

## Instalação e Configuração Inicial

** Passo 1: Instalação do Python **

Instale o Python 3.8 ou superior. O download pode ser realizado no site oficial do Python: https://www.python.org/

** Passo 2: Download da Ferramenta de Migração de Dados **

Faça o clone do repositório da Ferramenta de Migração de Dados do GitHub ou faça o download dos arquivos através do link:
https://github.com/Cosamores/gcp-migration-app


** Passo 3: Instalação das Dependências **

Navegue até o diretório onde os arquivos da Ferramenta de Migração de Dados foram baixados/clonados, abra um terminal nesta localização e execute o seguinte comando para instalar todas as dependências necessárias:

```
pip install -r requirements.txt
```

**Passo 4: Configuração da Chave do Google Cloud**

Para usar as APIs do Google Cloud como BigQuery ou Google Cloud Storage a partir de um script Python, você precisa autenticar seu aplicativo. A maneira mais comum de fazer isso é usando um arquivo de chave de serviço, que é um arquivo JSON que você baixa do Google Cloud Console. Este arquivo contém as credenciais que seu aplicativo usará para autenticar suas solicitações.

Aqui estão os passos gerais para criar e usar um arquivo de chave de serviço:

1. No Google Cloud Console, selecione seu projeto.

2. Navegue até IAM & Admin > Service Accounts.

3. Clique em Create Service Account, dê um nome e uma descrição para a conta de serviço e clique em Create.

4. Na seção Grant this service account access to project, adicione os papéis que sua conta de serviço precisará. Para este caso, você provavelmente precisará de papéis como BigQuery Data Editor e Storage Object Viewer. Clique em Continue e depois em Done.

5. Encontre a conta de serviço que você acabou de criar na lista, e clique no ícone de três pontos à direita e escolha Manage keys.

6. Clique em Add Key, e depois Create new key. Escolha JSON como o tipo de chave e clique em Create. Seu arquivo de chave será baixado automaticamente.

7. Agora você pode usar esse arquivo de chave em seu script Python para autenticar suas solicitações, porém ainda será necessário adicioná-la à aplicação.

8. No aplicativo, vá até a aba 'Configuração de GCP'.

9. Clique no botão 'Selecionar' ao lado de 'Arquivo de Chave GCP' e escolha o arquivo de chave de serviço JSON que você baixou do Google Cloud Console. 

10.Clique no botão “Abrir”, o caminho da chave deverá ser mostrado no campo correspondente.

Agora, o aplicativo usará automaticamente essas credenciais para autenticar todas as solicitações feitas para o Google Cloud.


