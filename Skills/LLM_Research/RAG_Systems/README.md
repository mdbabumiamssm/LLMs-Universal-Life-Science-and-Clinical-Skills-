# Retrieval Augmented Generation (RAG)

**Category:** LLM Research / Architectures
**Difficulty:** Intermediate

## Overview
RAG is a technique to optimize the output of an LLM by referencing an authoritative knowledge base outside of its training data before generating a response.

## Core Components

1.  **Retrieval:** Searching a database (usually a Vector Database) for content relevant to the user's query.
2.  **Augmentation:** Combining the retrieved content with the original user query into a coherent prompt.
3.  **Generation:** Sending the augmented prompt to the LLM to generate the final answer.

## Why use RAG?
*   **Accuracy:** Reduces hallucinations by grounding answers in facts.
*   **Freshness:** Allows the LLM to access up-to-date information without retraining.
*   **Privacy:** Enables the use of private/proprietary data.

## Implementation (simple_rag.py)
This module implements a "from scratch" RAG pipeline to demonstrate the mathematics of **Cosine Similarity** and the flow of data, without relying on "black box" libraries.

## Advanced Patterns (advanced_rag_patterns.py)
Moving beyond simple similarity search, this module implements SOTA techniques:

### 1. HyDE (Hypothetical Document Embeddings)
Instead of embedding the user's *question*, we ask an LLM to hallucinate a *perfect answer*, embed that answer, and search for documents matching the answer's vector.
*   **Problem Solved:** User queries are often short/poor ("p53?"), while documents are detailed. HyDE bridges this semantic gap.

### 2. Contextual Reranking
A two-stage retrieval process. First, retrieve a broad set of documents (e.g., top 50) using vector search. Then, use a specialized model (Cross-Encoder or LLM) to re-score and re-order them based on deep semantic relevance.
*   **Problem Solved:** Vector search is fast but "fuzzy". Reranking is slow but precise. Combining them gives the best of both worlds.

## Real-World Stack
In production, this pattern is implemented using:
*   **Orchestration:** LangChain, LlamaIndex
*   **Vector DB:** Pinecone, Milvus, Chroma, pgvector
*   **Embeddings:** OpenAI `text-embedding-3`, HuggingFace `all-MiniLM-L6-v2`
