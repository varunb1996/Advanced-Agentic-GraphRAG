import json
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="embeddings/chroma_db")

collection = client.get_or_create_collection("knowledge_base")

with open("data/processed/documents.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

for idx, doc in enumerate(docs):

    embedding = model.encode(doc["content"]).tolist()

    collection.add(
        ids=[str(idx)],
        documents=[doc["content"]],
        embeddings=[embedding],
        metadatas=[{
            "source": doc["source"],
            "type": doc["type"],
            "filename": doc["filename"],
            "folder": doc["folder"],
            "chunk_id": doc["chunk_id"]
        }]
    )

print("Embeddings stored successfully")