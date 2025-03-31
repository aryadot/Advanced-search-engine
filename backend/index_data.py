from backend.config import es, INDEX_NAME

# Sample documents to index
documents = [
    {"title": "Document 1", "content": "This is the first document."},
    {"title": "Document 2", "content": "This is another document about search engines."},
    {"title": "Advanced Search", "content": "This explains advanced search techniques."}
]

if not es.indices.exists(index=INDEX_NAME):
    es.indices.create(index=INDEX_NAME)

for doc in documents:
    es.index(index=INDEX_NAME, body=doc)

print("Documents indexed successfully.")
