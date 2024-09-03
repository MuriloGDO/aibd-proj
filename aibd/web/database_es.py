from elasticsearch import Elasticsearch


ELASTIC_PASSWORD = "trabalho_bd"

# Create the client instance
client = Elasticsearch(
    "https://es01:9200",
    ca_certs="/code/certs/ca/ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

def insert(table, data):
    client.index(index=table, document=data)

# def get_units():
#     client.search(index='instituicoes', )

# Tabela Instituicoes
{
    "id": "123",
    "nome": "nome_instituicao",
    "endereco": "endereco",
    "numero_de_vagas": 123,
    "localizacao": ""
}


# Tabela funcionarios
{
    "nome": "nome",
    "cpf": "",
    "instituicao": { # funcionarios.instituicao.id = 123
        "id": "123",
        "nome": "nome_instituicao"
    },
    "voluntario": false,
    "professor": false
}

# Aluno
{
    "nome": "nome",
    "cpf": "cpf",
    "renda": "",
    "data_de_nascimento": "dd/mm/yyyy",
    "instituicao": {
        "id": "123"
    },
    "responsavel": {
        "id": "123",
        "nome": "nome_responsavel"
    }
}

# Responsavel
{
    "nome": "nome",
    "telefone": "telefone"
}

# Aulas
{
    "hora_fim": "123",
    "materia": "materia",
    "hora_inicio": "123",
    "numero_da_sala": "123",
    "professor": {
        "id": "123",
    },
    "alunos": [
        {
            "id": "123"
        },
        {
            "id": "1234"
        },
        {
            "id": "1235"
        },
        {
            "id": "1236"
        },
    ]
}

# Simulados
{
    "professor": {
        "id": "123"
    },
    "alunos": [
        {
            "id": "123",
            "nota": "10"
        },
        {
            "id": "123",
            "nota": "9"
        },
        {
            "id": "123",
            "nota": "8"
        },
        {
            "id": "123",
            "nota": "7"
        },
    ],
    "aula": {
        "id": "123"
    }
}

# Financiadores
{
    "cpf_or_cnpj": "cnpj",
    "atividade_exercida": "atividade",
    "nome": "nome",
    "instituicoes_financiadas": [
        {
            "id": "id",
            "valor": "123"
        },
        {
            "id": "id",
            "valor": "124"
        },
        {
            "id": "id",
            "valor": "125"
        },
        {
            "id": "id",
            "valor": "126"
        },
    ]
}