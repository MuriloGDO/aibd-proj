# aibd-proj
Repositório para o trabalho final de AIBD

### Requisitos
- Python 3.x
- Django

### Instalação e Execução
1. Clone o repositório:

``` bash
    git clone https://github.com/MuriloGDO/aibd-proj.git
    cd aibd-proj
```
2. Criar e ativar um ambiente virtual (utilizando git bash):

```bash
    python -m venv env
    source env/Scripts/activate
```

3. Instalar as dependências:

```bash
    pip install -r requirements.txt
```

4. Iniciar o servidor:

```bash
    cd aibd/
    python manage.py runserver
```

5. Acesse a aplicação no navegador:

Abra http://localhost:8000.



## Docker

### env file
Crie um arquivo chamado '.env' e coloque as chaves abaixo dentro dele

```
# Project namespace (defaults to the current folder name if not set)
#COMPOSE_PROJECT_NAME=myproject


# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=trabalho_bd


# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=trabalho_bd


# Version of Elastic products
STACK_VERSION=8.15.0


# Set the cluster name
CLUSTER_NAME=docker-cluster


# Set to 'basic' or 'trial' to automatically start the 30-day trial
LICENSE=basic
#LICENSE=trial


# Port to expose Elasticsearch HTTP API to the host
ES_PORT=9200


# Port to expose Kibana to the host
KIBANA_PORT=5601


# Increase or decrease based on the available host memory (in bytes)
ES_MEM_LIMIT=1073741824
KB_MEM_LIMIT=1073741824
LS_MEM_LIMIT=1073741824


# SAMPLE Predefined Key only to be used in POC environments
ENCRYPTION_KEY=c34d38b3a14956121ff2170e5030b471551370178f43e5626eec58b04a30fae2

```

### Rodando o projeto
Baixe o docker
Instale o docker compose
No terminal, acesse a pasta 'app'  e digite `docker compose up`
Após 10 minutos acesse o Kibana dashboard via localhost:5061
Usuário: elastic // Senha: trabalho_bd
