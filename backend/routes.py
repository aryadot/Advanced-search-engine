from flask import request, jsonify
from backend import app
from flask_cors import CORS 
from backend.config import es, INDEX_NAME

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    print(f"Received query: {query}")  # Log the incoming query
    try:
        body = {
            'query': {
                'bool': {
                    'must': [{'match': {'content': query}}],
                    'should': [{'match': {'title': query}}]
                }
            },
            'highlight': {
                'fields': {
                    'content': {}
                }
            }
        }
        res = es.search(index=INDEX_NAME, body=body)
        print(f"Elasticsearch response: {res}")  # Log the response from Elasticsearch
        results = [
            {
                'title': hit['_source']['title'],
                'content': hit['_source']['content'],
                'score': hit['_score'],
                'highlight': hit.get('highlight', {})
            }
            for hit in res['hits']['hits']
        ]
        return jsonify(results)
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred"}), 500
