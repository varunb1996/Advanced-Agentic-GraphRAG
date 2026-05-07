import streamlit as st
import requests

st.title("Advanced Agentic GraphRAG")

query = st.text_input("Ask a question")

if st.button("Search"):

    response = requests.get(
        "http://127.0.0.1:8000/query",
        params={"q": query}
    )

    data = response.json()

    documents = data["documents"][0]
    metadatas = data["metadatas"][0]
    distances = data["distances"][0]

    for i in range(len(documents)):

        st.subheader(f"Result {i+1}")

        st.write(f"Source: {metadatas[i]['source']}")
        st.write(f"Type: {metadatas[i]['type']}")
        st.write(f"Folder: {metadatas[i]['folder']}")
        st.write(f"Similarity: {round(distances[i], 4)}")

        st.text_area(
            "Content",
            documents[i],
            height=250
        )

        st.divider()