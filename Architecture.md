# Architecture Overview

## System Goal

Advanced-Agentic-GraphRAG is a lightweight production-style GraphRAG system designed to combine:

- Semantic Retrieval
- Graph-Based Knowledge Relationships
- Agentic APIs
- Repository Intelligence
- Technical Document Understanding

using fully open-source tools and local-first workflows.

The project acts as a foundation for engineering knowledge systems, AI-assisted development pipelines, and future agentic coding environments.

---

# High-Level System Architecture

```text
                    ┌────────────────────┐
                    │      User Query     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   Streamlit UI      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   FastAPI Backend   │
                    └─────────┬──────────┘
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
    ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
    │ Retrieval Layer │ │ Graph Layer    │ │ Agent Layer    │
    └────────────────┘ └────────────────┘ └────────────────┘
              │               │                │
              ▼               ▼                ▼
    ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
    │ ChromaDB       │ │ NetworkX Graph │ │ LangGraph Flow │
    │ Vector Store   │ │ Relationships  │ │ Multi-Agent    │
    └────────────────┘ └────────────────┘ └────────────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ OpenRouter LLM API │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   Final Response    │
                    └────────────────────┘
```

---

# Core Components

---

## 1. Document Ingestion Layer

### Purpose

Handles ingestion of:
- PDF files
- Technical documentation
- Source-code repositories

### Responsibilities

- Text extraction
- Intelligent chunking
- Metadata enrichment
- Repository parsing

### Main Files

```text
ingest.py
update_index.py
```

---

## 2. Embedding Pipeline

### Purpose

Converts chunks into semantic vector embeddings.

### Technologies

- Sentence Transformers
- HuggingFace Embedding Models

### Responsibilities

- Embedding generation
- Semantic representation
- Vector preparation

### Main Files

```text
embed.py
```

---

## 3. Vector Database Layer

### Purpose

Stores semantic embeddings for retrieval.

### Technology

- ChromaDB

### Responsibilities

- Similarity search
- Context retrieval
- Persistent vector storage

### Main Files

```text
retrieval.py
```

---

## 4. Graph Relationship Layer

### Purpose

Builds graph-aware relationships between:
- documents
- repositories
- dependencies
- metadata
- contextual entities

### Technology

- NetworkX

### Responsibilities

- Relationship mapping
- Graph traversal
- Knowledge linking

### Main Files

```text
graph_builder.py
```

---

## 5. Agentic Workflow Layer

### Purpose

Coordinates retrieval and reasoning workflows.

### Technology

- LangGraph

### Responsibilities

- Multi-step reasoning
- Context orchestration
- Workflow routing
- Agent coordination

### Planned Agent Types

- Retrieval Agent
- Dependency Agent
- Summarizer Agent
- Router Agent
- Memory Agent

---

## 6. API Layer

### Purpose

Exposes backend services for querying the GraphRAG pipeline.

### Technology

- FastAPI

### Responsibilities

- REST APIs
- Query handling
- Workflow triggering
- Response serving

### Main Files

```text
api.py
```

---

## 7. Frontend Layer

### Purpose

Provides an interactive UI for querying the system.

### Technology

- Streamlit

### Responsibilities

- User interaction
- Query visualization
- Response rendering

### Main Files

```text
app.py
```

---

## 8. LLM Reasoning Layer

### Purpose

Generates intelligent responses using retrieved context.

### Technology

- OpenRouter APIs
- Free online LLMs
- Nvidia Nemotron / DeepSeek / Mixtral

### Responsibilities

- Contextual reasoning
- Answer generation
- Multi-context synthesis

---

## 9. MLflow Observability Layer

### Purpose

Tracks AI workflow lifecycle and experiments.

### Technology

- MLflow

### Responsibilities

- Experiment tracking
- Parameter logging
- Metrics monitoring
- Artifact tracking
- Workflow observability

### Tracked Components

- Embedding generation
- Retrieval execution
- Query latency
- Workflow runs
- Vector indexing metadata

---

# Workflow Execution Pipeline

## Step 1: Ingestion

```text
PDFs / Code Repositories
        ↓
Chunking + Metadata Extraction
```

---

## Step 2: Embedding Generation

```text
Text Chunks
        ↓
Sentence Transformers
        ↓
Vector Embeddings
```

---

## Step 3: Vector Storage

```text
Embeddings
        ↓
ChromaDB Storage
```

---

## Step 4: Graph Construction

```text
Metadata + Dependencies
        ↓
NetworkX Graph Relationships
```

---

## Step 5: Query Processing

```text
User Query
        ↓
FastAPI Endpoint
        ↓
Retrieval + Graph Traversal
```

---

## Step 6: Agentic Reasoning

```text
Retrieved Context
        ↓
LangGraph Workflow
        ↓
LLM Reasoning
```

---

## Step 7: Response Generation

```text
Reasoned Context
        ↓
Final Answer
        ↓
Streamlit UI
```

---

# Tech Stack

## Backend

- Python
- FastAPI

## Frontend

- Streamlit

## Retrieval

- ChromaDB
- Sentence Transformers

## Graph Intelligence

- NetworkX

## Agent Framework

- LangGraph

## LLM APIs

- OpenRouter
- Nvidia Nemotron
- DeepSeek
- Mixtral

## Observability

- MLflow

---

# Project Structure

```text
Advanced-Agentic-GraphRAG/
│
├── app.py
├── api.py
├── ingest.py
├── embed.py
├── retrieval.py
├── graph_builder.py
├── update_index.py
├── requirements.txt
├── README.md
├── architecture.md
│
├── data/
├── vectorstore/
├── graphs/
├── mlruns/
├── documents/
│
├── agents/
├── tools/
├── workflows/
└── utils/
```

---

# Future Improvements

- Neo4j integration
- Hybrid Retrieval (BM25 + Vector Search)
- Cross-repository GraphRAG
- Multi-agent autonomous workflows
- Tool-calling agents
- Persistent conversational memory
- Streaming responses
- Reranking pipelines
- Docker deployment
- Kubernetes orchestration
- CI/CD integration
- LangSmith tracing
- Knowledge graph expansion

---

# Design Philosophy

The system is intentionally designed as:

- Lightweight
- Modular
- Open-source-first
- Extensible
- Production-inspired
- Research-friendly

while remaining deployable on local hardware using free APIs and open tooling.
