from elasticsearch import Elasticsearch

# Elasticsearch connection
es = Elasticsearch("http://localhost:9200")
INDEX_NAME = "documents"  # Name of the index
