from fastapi import FastAPI

from retrieval import (
    search,
    search_by_type,
    get_related_nodes
)

app = FastAPI()


@app.get("/query")
def query_rag(q: str):

    return search(q)


@app.get("/query_code")
def query_code(q: str):

    return search_by_type(q, "code")


@app.get("/query_docs")
def query_docs(q: str):

    return search_by_type(q, "pdf")


@app.get("/related/{node_id}")
def related(node_id: int):

    return {
        "related_nodes": get_related_nodes(node_id)
    }