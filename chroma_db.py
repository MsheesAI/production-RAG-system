import chroma_db

client = chroma_db.Client()

collection_name = "my_collection"

collection = client.get_or_create_collection(name=collection_name)

documents = [
    {"id": "1", "text": "Hello world"},
    {"id": "2", "text": "How are you?"},
    {"id": "3", "text": "Goodbye!"}
]
for doc in documents:
  collection.upsert_document(ids =  doc['id'], texts = doc['text'])

query = "Hello world"
