#Ferramenta de migração de dados para o BigQuery - Documentação de uso

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

**Passo 1: Instalação do Python**

Instale o Python 3.8 ou superior. O download pode ser realizado no site oficial do Python: https://www.python.org/

**Passo 2: Download da Ferramenta de Migração de Dados**

Faça o clone do repositório da Ferramenta de Migração de Dados do GitHub ou faça o download dos arquivos.



**Passo 3: Instalação das Dependências**

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

7. Agora você pode usar esse arquivo de chave em seu script Python para autenticar suas solicitações. A maneira mais fácil de fazer isso é configurando a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS para o caminho do seu arquivo de chave. Você pode fazer isso em seu script Python da seguinte maneira:

```
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = “/path/to/your/service-account-file.json"

```

Substitua "/path/to/your/service-account-file.json" pelo caminho do seu arquivo de chave. Depois de definir esta variável de ambiente, as bibliotecas cliente do Google Cloud (como google.cloud.bigquery e google.cloud.storage) irão automaticamente usar estas credenciais para autenticar suas solicitações.

Lembre-se de manter seu arquivo de chave seguro, e não o compartilhe ou o envie para o controle de versão. Qualquer pessoa com acesso a este arquivo pode usar suas credenciais para fazer solicitações ao Google Cloud em nome de seu projeto.


# Uso da Ferramenta de Migração de Dados

## Conversão de Arquivos

Essa função converte arquivos XML e SAV para o formato CSV. O formato CSV (Comma-Separated Values) é um formato de arquivo que armazena dados tabulares (números e texto) em texto simples. Cada linha do arquivo é um registro de dados. Cada registro consiste em um ou mais campos, separados por vírgulas. A formalização dos dados em um formato comum, como o CSV, é crucial para garantir a interoperabilidade e a consistência dos dados.

###Passos para a conversão dos arquivos:

**Passo 1:** Selecione a aba 'Converter Arquivos'.
**Passo 2:** Clique no botão 'Selecionar' ao lado de 'Diretório de Entrada' e escolha o diretório que contém os arquivos XML/SAV.
**Passo 3:** Clique no botão 'Selecionar' ao lado de 'Diretório de Saída' e escolha o diretório onde os arquivos convertidos em CSV serão salvos.
**Passo 4:** Clique no botão 'Converter'. Uma mensagem será exibida ao final da operação.


## Upload para GCP

### Descrição do recurso

Essa função faz o upload de arquivos para um bucket do Google Cloud Storage (GCS). O Google Cloud Storage é um serviço de armazenamento de objetos flexível e escalonável para dados não estruturados. Os buckets do GCS são contêineres básicos que armazenam seus dados e mantêm a organização dos mesmos.
Os nomes dos buckets devem ser únicos em todo o GCS. Recomenda-se escolher um nome de bucket que reflita a estrutura organizacional de sua empresa para facilitar o gerenciamento. Para mais informações sobre o Google Cloud Storage e as melhores práticas, consulte a documentação oficial.

###Passos para o upload dos arquivos para o GCP:

**Passo 1:** Selecione a aba 'Upload para GCP'.
**Passo 2:** Preencha o campo 'Nome do Bucket' com o nome do bucket do Google Cloud Storage.
**Passo 3:** Clique no botão 'Selecionar' ao lado de 'Diretório de Origem' e escolha o diretório que contém os arquivos a serem carregados.
**Passo 4:** Clique no botão 'Upload'. Uma mensagem será exibida ao final da operação.


## Criação de Tabelas no Google BigQuery 

### Descrição do recurso

A ferramenta "Criação de Tabelas no BigQuery" é uma funcionalidade integrada à interface gráfica do usuário (GUI) que permite a criação de uma nova tabela no Google BigQuery a partir de um arquivo existente no Google Cloud Storage (GCS). Além disso, esta ferramenta permite ao usuário definir manualmente o esquema de tabela ou optar pela geração automática de esquema pelo BigQuery.

### Instruções de uso

1. **Seleção do ID do Conjunto de Dados:** No campo 'ID do Conjunto de Dados', insira o ID do conjunto de dados no qual você deseja criar a tabela. Esse ID é exclusivo para o conjunto de dados dentro do projeto do Google Cloud e pode ser encontrado na interface do BigQuery.

2. **Definição do ID da Tabela:** No campo 'ID da Tabela', insira o ID desejado para a nova tabela que será criada. Esse ID será exclusivo para a tabela dentro do conjunto de dados selecionado.

3. **Fornecimento da URI do Bucket:** No campo 'URI do Bucket', insira a URI do arquivo no GCS que contém os dados que você deseja carregar na nova tabela. A URI deve seguir o formato `gs://[bucket]/[nome_do_arquivo]`.

4. **Definição do Esquema da Tabela:** Você tem duas opções para definir o esquema da tabela: 

   4.1 **Esquema Automático:** Selecione a opção 'Automático' se desejar que o BigQuery gere automaticamente um esquema para a tabela com base nos dados do arquivo.

   4.2 **Esquema Personalizado:** Selecione a opção 'Personalizado' se desejar definir manualmente o esquema da tabela. Insira os nomes e tipos de dados das colunas conforme necessário.

5. **Criação da Tabela:** Clique no botão 'Criar' para iniciar o processo de criação da tabela. A ferramenta exibirá uma barra de progresso enquanto a tabela estiver sendo criada. Uma mensagem será exibida na interface quando a tabela for criada com sucesso ou se houver algum erro durante o processo.

### Notas adicionais:

- A ferramenta foi projetada para criar uma nova tabela a cada execução. Se você deseja adicionar dados a uma tabela existente, deverá usar funções diferentes.
- Certifique-se de que você tenha as permissões necessárias para criar tabelas no conjunto de dados especificado e para acessar o arquivo no GCS.
- Erros comuns que podem ocorrer durante a criação da tabela incluem fornecer uma URI de arquivo inválida, um ID de conjunto de dados inválido, um ID de tabela inválido ou um esquema de tabela inválido. Verifique cuidadosamente todas as entradas antes de tentar criar a tabela.

## Seção de Resolução de Problemas

Antes de abrir um ticket de suporte, verifique se todas as dependências foram instaladas corretamente e se você está usando a versão correta do Python. Além disso, confira se a chave do Google Cloud foi configurada corretamente como uma variável de ambiente.

## FAQs

Essa seção pode ser usada para responder às perguntas mais frequentes dos usuários sobre a Ferramenta de Migração de Dados.



IFSP Caraguatatuba, 5/2023