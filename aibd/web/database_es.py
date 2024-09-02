from elasticsearch import Elasticsearch


ELASTIC_PASSWORD = "trabalho_bd"

# Create the client instance
client = Elasticsearch(
    "https://es01:9200",
    ca_certs="/code/certs/ca/ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)


print(client.info())