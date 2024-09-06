from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "trabalho_bd"

# Create the client instance
client = Elasticsearch(
    "https://es01:9200",
    ca_certs="/code/certs/ca/ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

def get_units():
    # Consulta para buscar todas as instituições
    response = client.search(index="instituicoes", body={"query": {"match_all": {}}})
    print(response)
    # Mostrar resultados
    units = []
    for hit in response["hits"]["hits"]:
        unit = {
            "id": hit["_id"],
            **hit["_source"]
        }
        units.append(unit)
        # print(hit["_source"])
    return units

def get_unit(unit_id):
    # Consulta para buscar uma instituição
    response = client.get(index="instituicoes", id=unit_id)
    unit = {
        "id": unit_id,
        **response["_source"]
    }
    return unit

def insert_student(aluno_json, responsavel_json):
    parent_id = insert_parents(responsavel_json)
    aluno_json["responsavel"] = {"id": parent_id}
    client.index(index="aluno", document=aluno_json)
    decrement_vagas(aluno_json["instituicao"]["id"])

def insert_parents(responsavel_json):
    res = client.index(index="responsavel", document=responsavel_json)
    return res["_id"]

def update_unit(unit_id, data):
    client.index(index="instituicoes", id=unit_id, document=data)

def decrement_vagas(unit_id):
    unit = get_unit(unit_id)
    unit["numero_de_vagas"] -= 1
    del unit["id"]
    update_unit(unit_id, unit)

def insert(table, data):
    return client.index(index=table, document=data)

def count_students(unit_id):
    query = {
        "size": 0,  # Não precisamos dos documentos, apenas da contagem
        "query": {
            "nested": {
                "path": "instituicao",
                "query": {
                    "term": {
                        "instituicao.id.keyword": unit_id
                    }
                }
            }
        }
    }
    try:
        response = client.search(index="aluno", body=query)
        return response["hits"]["total"]["value"]
    except Exception as e:
        print(f"Erro ao contar alunos: {e}")
        return 0
    
def get_distance(unit_id, lat, lon):
    query = {
        "query": {
            "bool": {
                "filter": {
                    "term": {
                        "_id": unit_id
                    }
                }
            }
        },
        "sort": [
            {
                "_geo_distance": {
                    "localizacao": {
                        "lat": lat,
                        "lon": lon
                    },
                    "order": "asc",
                    "unit": "km"
                }
            }
        ]
    }
    response = client.search(index="instituicoes", body=query)
    if response['hits']['hits']:
            distance = response['hits']['hits'][0]['sort'][0]
            return round(distance, 2)
    else:
            return None
    
def list_teachers(unit_id):
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "term": { "professor": True }
                    },
                    {
                        "nested": {
                            "path": "instituicao",
                            "query": {
                                "bool": {
                                    "filter": [
                                        {
                                            "term": { "instituicao.id.keyword": unit_id }
                                        }
                                    ]
                                }
                            }
                        }
                    }
                ]
            }
        }
    }

    response = client.search(index="funcionarios", body=query)
    professores = [hit["_source"] for hit in response["hits"]["hits"]]
    return professores

def list_voluntarios(unit_id):
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "term": { "voluntario": True }
                    },
                    {
                        "nested": {
                            "path": "instituicao",
                            "query": {
                                "bool": {
                                    "filter": [
                                        {
                                            "term": { "instituicao.id.keyword": unit_id }
                                        }
                                    ]
                                }
                            }
                        }
                    }
                ]
            }
        }
    }

    response = client.search(index="funcionarios", body=query)
    professores = [hit["_source"] for hit in response["hits"]["hits"]]
    return professores

def list_financiadores(unit_id):
    query = {
        "query": {
            "bool": {
                "filter": {
                    "term": {
                        "instituicoes_financiadas.instituicao_id.keyword": unit_id
                    }
                }
            }
        }
    }

    response = client.search(index="financiadores", body=query)
    financiadores = [hit["_source"] for hit in response["hits"]["hits"]]
    return financiadores

def media_investimento(unit_id):
    query = {
        "query": {
            "bool": {
                "filter": {
                    "term": {
                        "instituicoes_financiadas.instituicao_id.keyword": unit_id
                    }
                }
            }
        },
        "aggs": {
            "filtered_values": {
                "filter": {
                    "term": {
                        "instituicoes_financiadas.instituicao_id.keyword": unit_id
                    }
                },
                "aggs": {
                    "average_value": {
                        "avg": {
                            "field": "instituicoes_financiadas.valor"
                        }
                    }
                }
            }
        }
    }
    response = client.search(index="financiadores", body=query)
    media_investimento = response['aggregations']['filtered_values']['average_value']['value']
    
    return round(media_investimento, 2)

# def get_units():
#     client.search(index='instituicoes', )

# # Tabela Instituicoes
# {
#     "id": "123",
#     "nome": "nome_instituicao",
#     "endereco": "endereco",
#     "numero_de_vagas": 123,
#     "localizacao": ""
# }


# # Tabela funcionarios
# {
#     "nome": "nome",
#     "cpf": "",
#     "instituicao": { # funcionarios.instituicao.id = 123
#         "id": "123",
#         "nome": "nome_instituicao"
#     },
#     "voluntario": false,
#     "professor": false
# }

# # Aluno
# {
#     "nome": "nome",
#     "cpf": "cpf",
#     "renda": "",
#     "data_de_nascimento": "dd/mm/yyyy",
#     "instituicao": {
#         "id": "123"
#     },
#     "responsavel": {
#         "id": "123",
#         "nome": "nome_responsavel"
#     }
# }

# # Responsavel
# {
#     "nome": "nome",
#     "telefone": "telefone"
# }

# # Aulas
# {
#     "hora_fim": "123",
#     "materia": "materia",
#     "hora_inicio": "123",
#     "numero_da_sala": "123",
#     "professor": {
#         "id": "123",
#     },
#     "alunos": [
#         {
#             "id": "123"
#         },
#         {
#             "id": "1234"
#         },
#         {
#             "id": "1235"
#         },
#         {
#             "id": "1236"
#         },
#     ]
# }

# # Simulados
# {
#     "professor": {
#         "id": "123"
#     },
#     "alunos": [
#         {
#             "id": "123",
#             "nota": "10"
#         },
#         {
#             "id": "123",
#             "nota": "9"
#         },
#         {
#             "id": "123",
#             "nota": "8"
#         },
#         {
#             "id": "123",
#             "nota": "7"
#         },
#     ],
#     "aula": {
#         "id": "123"
#     }
# }

# # Financiadores
# {
#     "cpf_or_cnpj": "cnpj",
#     "atividade_exercida": "atividade",
#     "nome": "nome",
#     "instituicoes_financiadas": [
#         {
#             "id": "id",
#             "valor": "123"
#         },
#         {
#             "id": "id",
#             "valor": "124"
#         },
#         {
#             "id": "id",
#             "valor": "125"
#         },
#         {
#             "id": "id",
#             "valor": "126"
#         },
#     ]
# }
