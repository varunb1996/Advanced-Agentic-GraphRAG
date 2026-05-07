import json
import networkx as nx

G = nx.Graph()

COMMON_TERMS = [
    "retriever",
    "embedding",
    "vectorstore",
    "agent",
    "prompt",
    "memory"
]

with open("data/processed/documents.json", "r", encoding="utf-8") as f:
    docs = json.load(f)


# -------------------------------
# ADD NODES
# -------------------------------

for idx, doc in enumerate(docs):

    G.add_node(
        idx,
        source=doc["source"],
        type=doc["type"],
        filename=doc["filename"],
        folder=doc["folder"]
    )


# -------------------------------
# ADD EDGES
# -------------------------------

for i in range(len(docs)):

    for j in range(i + 1, len(docs)):

        for term in COMMON_TERMS:

            if (
                term in docs[i]["content"].lower()
                and
                term in docs[j]["content"].lower()
            ):

                G.add_edge(
                    i,
                    j,
                    relation=term
                )


print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

nx.write_gml(G, "graph/knowledge_graph.gml")