import chromadb
import networkx as nx
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="embeddings/chroma_db")

collection = client.get_collection("knowledge_base")

G = nx.read_gml("graph/knowledge_graph.gml")


# ---------------------------------
# GENERAL SEARCH
# ---------------------------------

def search(query, top_k=3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results


# ---------------------------------
# FILTERED SEARCH
# ---------------------------------

def search_by_type(query, doc_type):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        where={"type": doc_type}
    )

    return results


# ---------------------------------
# GRAPH RELATIONSHIPS
# ---------------------------------

def get_related_nodes(node_id):

    neighbors = list(G.neighbors(str(node_id)))

    return neighbors


# ---------------------------------
# TEST MODE
# ---------------------------------

if __name__ == "__main__":

    query = input("Enter query: ")

    results = search(query)

    print(results)