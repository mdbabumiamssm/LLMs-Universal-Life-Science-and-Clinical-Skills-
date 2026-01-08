"""
Advanced RAG Patterns: HyDE and Contextual Reranking

This module implements State-of-the-Art (SOTA) Retrieval Augmented Generation (RAG) techniques
to improve the accuracy and relevance of LLM responses in specialized domains (like biomedicine).

Implemented Patterns:
1. HyDE (Hypothetical Document Embeddings): Generates a fake "perfect" answer to the query, 
   embeds it, and uses that vector to find real documents. Great for poorly phrased queries.
2. Contextual Reranking: Re-scores retrieved documents based on their relevance to the 
   query using a cross-encoder or LLM-based scorer.
"""

from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod
import math

# --- Interfaces ---

class Embedder(ABC):
    """Abstract base class for embedding models."""
    @abstractmethod
    def embed(self, text: str) -> List[float]:
        pass

class VectorStore(ABC):
    """Abstract base class for vector storage."""
    @abstractmethod
    def search(self, query_vector: List[float], k: int = 5) -> List[Dict[str, Any]]:
        pass

class LLM(ABC):
    """Abstract base class for LLM."""
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

# --- Implementations ---

class HyDERetriever:
    """
    Hypothetical Document Embeddings (HyDE) Retriever.
    
    Paper: https://arxiv.org/abs/2212.10496
    Logic: Query -> LLM -> Hypothetical Answer -> Embedding -> Vector Search -> Real Docs
    """
    
    def __init__(self, llm: LLM, embedder: Embedder, vector_store: VectorStore):
        self.llm = llm
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Execute the HyDE retrieval process.
        """
        # Step 1: Generate Hypothetical Document
        # We ask the LLM to write a paragraph that *would* answer the query.
        hyde_prompt = f"""
        Please write a scientific passage to answer the question below. 
        Do not answer the question directly, but write the content that a perfect 
        textbook or research paper would contain to answer it.
        
        Question: {query}        
        Passage:
        """
        hypothetical_doc = self.llm.generate(hyde_prompt)
        print(f"[HyDE] Generated Hypothetical Doc: {hypothetical_doc[:50]}...")
        
        # Step 2: Encode the hypothetical document
        # The vector of this "fake" answer is often closer to the "real" answer 
        # than the vector of the raw query is.
        query_vector = self.embedder.embed(hypothetical_doc)
        
        # Step 3: Retrieve real documents using this vector
        results = self.vector_store.search(query_vector, k=k)
        
        return results

class ContextualReranker:
    """
    Reranks a list of retrieved documents based on relevance to the query.
    """
    
    def __init__(self, llm: Optional[LLM] = None):
        self.llm = llm

    def rerank(self, query: str, documents: List[Dict[str, Any]], top_n: int = 3) -> List[Dict[str, Any]]:
        """
        Rerank documents using a "Listwise" approach (asking LLM to rank them).
        """
        if not documents:
            return []
            
        # If no LLM provided, just return top_n of original (identity)
        if not self.llm:
            return documents[:top_n]
            
        print(f"[Reranker] Reranking {len(documents)} documents for query: {query}")
        
        # Prompt engineering for reranking
        docs_text = "\n".join([
            f"Doc {i+1}: {doc.get('content', '')[:200]}..." 
            for i, doc in enumerate(documents)
        ])
        
        prompt = f"""
        You are an expert relevance ranker. Given the query and the list of documents below, 
        rank the documents from most relevant to least relevant.
        
        Query: {query}
        
        Documents:
        {docs_text}
        
        Return ONLY a list of numbers representing the rank order (e.g., "2, 1, 3").
        """
        
        response = self.llm.generate(prompt)
        
        # Parse response (Mock logic for safety if parsing fails)
        try:
            # simple parsing assuming "2, 1, 3" format
            indices = [int(x.strip()) - 1 for x in response.split(',') if x.strip().isdigit()]
            
            # Reorder documents
            reranked = []
            seen = set()
            for idx in indices:
                if 0 <= idx < len(documents) and idx not in seen:
                    reranked.append(documents[idx])
                    seen.add(idx)
            
            # Add remaining documents that weren't ranked
            for i, doc in enumerate(documents):
                if i not in seen:
                    reranked.append(doc)
                    
            return reranked[:top_n]
            
        except Exception as e:
            print(f"[Reranker] Parsing failed: {e}. Returning original order.")
            return documents[:top_n]

# --- Mocks for Demonstration ---

class MockEmbedder(Embedder):
    def embed(self, text: str) -> List[float]:
        # Return random vector of dim 4
        import random
        return [random.random() for _ in range(4)]

class MockVectorStore(VectorStore):
    def search(self, query_vector: List[float], k: int = 5) -> List[Dict[str, Any]]:
        return [
            {"id": "doc1", "content": "The p53 protein acts as a tumor suppressor.", "score": 0.9},
            {"id": "doc2", "content": "Mitochondria are the powerhouse of the cell.", "score": 0.8},
            {"id": "doc3", "content": "CRISPR-Cas9 is a gene editing tool.", "score": 0.75},
            {"id": "doc4", "content": "DNA is composed of four nucleotides.", "score": 0.6}
        ][:k]

class MockLLM(LLM):
    def generate(self, prompt: str) -> str:
        if "scientific passage" in prompt:
            return "Tumor suppressors regulate cell division and prevent cancer."
        if "rank the documents" in prompt:
            return "1, 3, 2, 4"
        return "Mock response"

# --- Usage Example ---

if __name__ == "__main__":
    # Setup dependencies
    llm = MockLLM()
    embedder = MockEmbedder()
    store = MockVectorStore()
    
    # Initialize HyDE
    hyde = HyDERetriever(llm, embedder, store)
    
    # Initialize Reranker
    reranker = ContextualReranker(llm)
    
    query = "How do tumor suppressors work?"
    
    print(f"Query: {query}")
    
    # 1. HyDE Retrieval
    print("\n--- Step 1: HyDE Retrieval ---")
    initial_docs = hyde.retrieve(query, k=4)
    for doc in initial_docs:
        print(f"Retrieved: {doc['id']} (Score: {doc['score']})")
        
    # 2. Reranking
    print("\n--- Step 2: Contextual Reranking ---")
    final_docs = reranker.rerank(query, initial_docs, top_n=2)
    for i, doc in enumerate(final_docs):
        print(f"Rank {i+1}: {doc['id']} - {doc['content']}")
