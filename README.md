## Advanced Agentic GraphRAG System

A lightweight production-style GraphRAG system built using fully open-source resources to combine semantic retrieval, graph-based knowledge relationships, and agentic APIs across technical documents and code repositories.

The project supports:
PDF and code repository ingestion
Intelligent chunking and metadata enrichment
Semantic embeddings with Sentence Transformers
ChromaDB vector storage
Graph-based relationships using NetworkX
FastAPI backend APIs
Streamlit interactive UI
Agent-oriented retrieval endpoints
Designed as a foundation for evolving knowledge systems, engineering collaboration, and future integration with agentic coding tools such as Claude Code and Codex.


## Tech Stack
Python
FastAPI
Streamlit
ChromaDB
Sentence Transformers
NetworkX
PyPDF

## Run the project
python ingest.py
python embed.py
python graph_builder.py
python -m uvicorn api:app --reload
python -m streamlit run app.py
