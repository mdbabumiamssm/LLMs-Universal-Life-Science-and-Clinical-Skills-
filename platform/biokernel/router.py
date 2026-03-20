# Copyright (c) 2026 MD Babu Mia, PhD <md.babu.mia@mssm.edu>
# Icahn School of Medicine at Mount Sinai. All Rights Reserved.

"""
Semantic Skill Router for the BioKernel.

Matches user queries to the most appropriate registered skill using
a combination of:
1. **TF-IDF cosine similarity** (lightweight, no GPU needed)
2. **Keyword overlap** as a fallback
3. **Exact skill_id matching** when the user specifies a skill

This approach avoids requiring embedding model downloads while still
providing substantially better routing than keyword matching alone.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import Dict, List, Optional, Tuple

from platform.observability import get_logger
from platform.schema.io_types import SkillMetadata

logger = get_logger("router")


class SkillRouter:
    """
    Routes natural-language queries to the best matching skill.

    Uses a lightweight TF-IDF approach for semantic similarity that
    runs in pure Python with no external dependencies.
    """

    def __init__(self, similarity_threshold: float = 0.35) -> None:
        self.skills: Dict[str, SkillMetadata] = {}
        self.similarity_threshold = similarity_threshold
        self._idf: Dict[str, float] = {}
        self._skill_vectors: Dict[str, Dict[str, float]] = {}
        self._dirty = True

    def register_skill(self, skill: SkillMetadata) -> None:
        """Add or update a skill in the routing index."""
        self.skills[skill.skill_id] = skill
        self._dirty = True

    def remove_skill(self, skill_id: str) -> None:
        """Remove a skill from the routing index."""
        self.skills.pop(skill_id, None)
        self._skill_vectors.pop(skill_id, None)
        self._dirty = True

    def route(
        self,
        query: str,
        *,
        skill_id: Optional[str] = None,
        top_k: int = 5,
    ) -> List[Tuple[str, float]]:
        """
        Route a query to the best matching skills.

        Args:
            query: Natural-language user query.
            skill_id: If provided, short-circuit to this skill (exact match).
            top_k: Number of top matches to return.

        Returns:
            List of (skill_id, score) tuples, sorted descending by score.
        """
        # Exact match override
        if skill_id and skill_id in self.skills:
            return [(skill_id, 1.0)]

        if not self.skills:
            return []

        # Rebuild index if needed
        if self._dirty:
            self._rebuild_index()

        query_tokens = self._tokenize(query)
        query_vec = self._tfidf_vector(query_tokens)

        scored: List[Tuple[str, float]] = []
        for sid, skill_vec in self._skill_vectors.items():
            sim = self._cosine_similarity(query_vec, skill_vec)
            if sim >= self.similarity_threshold:
                scored.append((sid, sim))

        # Sort by score descending
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def get_best_match(self, query: str, skill_id: Optional[str] = None) -> Optional[str]:
        """Return the single best skill_id, or None if nothing matches."""
        matches = self.route(query, skill_id=skill_id, top_k=1)
        return matches[0][0] if matches else None

    # -- Index building -------------------------------------------------------

    def _rebuild_index(self) -> None:
        """Rebuild the TF-IDF index from all registered skills."""
        # Collect all documents (one per skill)
        documents: Dict[str, List[str]] = {}
        for sid, skill in self.skills.items():
            text = self._skill_to_text(skill)
            documents[sid] = self._tokenize(text)

        # Compute IDF
        n_docs = len(documents)
        doc_freq: Counter[str] = Counter()
        for tokens in documents.values():
            unique_tokens = set(tokens)
            for token in unique_tokens:
                doc_freq[token] += 1

        self._idf = {
            token: math.log((n_docs + 1) / (freq + 1)) + 1
            for token, freq in doc_freq.items()
        }

        # Compute TF-IDF vectors for each skill
        self._skill_vectors = {}
        for sid, tokens in documents.items():
            self._skill_vectors[sid] = self._tfidf_vector(tokens)

        self._dirty = False
        logger.info("Router index rebuilt", n_skills=n_docs)

    def _tfidf_vector(self, tokens: List[str]) -> Dict[str, float]:
        """Compute a TF-IDF vector for a list of tokens."""
        tf = Counter(tokens)
        total = len(tokens) or 1
        vec: Dict[str, float] = {}
        for token, count in tf.items():
            idf = self._idf.get(token, 1.0)
            vec[token] = (count / total) * idf
        return vec

    @staticmethod
    def _cosine_similarity(a: Dict[str, float], b: Dict[str, float]) -> float:
        """Cosine similarity between two sparse vectors."""
        # Dot product over shared keys
        dot = sum(a[k] * b[k] for k in a if k in b)
        mag_a = math.sqrt(sum(v * v for v in a.values()))
        mag_b = math.sqrt(sum(v * v for v in b.values()))
        if mag_a == 0 or mag_b == 0:
            return 0.0
        return dot / (mag_a * mag_b)

    @staticmethod
    def _skill_to_text(skill: SkillMetadata) -> str:
        """Combine all skill metadata into a single searchable text."""
        parts = [
            skill.name,
            skill.description,
            skill.skill_id.replace("-", " "),
            " ".join(skill.tags),
            " ".join(skill.capabilities),
            skill.category or "",
        ]
        return " ".join(parts)

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        """Simple whitespace + punctuation tokenizer with lowercasing."""
        text = text.lower()
        # Split on non-alphanumeric characters
        tokens = re.findall(r"[a-z0-9]+", text)
        # Remove very short tokens and common stop words
        stop_words = {
            "the", "a", "an", "is", "are", "was", "were", "be", "been",
            "being", "have", "has", "had", "do", "does", "did", "will",
            "would", "could", "should", "may", "might", "can", "shall",
            "to", "of", "in", "for", "on", "with", "at", "by", "from",
            "as", "into", "through", "during", "before", "after", "above",
            "below", "and", "but", "or", "nor", "not", "so", "yet",
            "both", "either", "neither", "each", "every", "all", "any",
            "this", "that", "these", "those", "it", "its", "you", "your",
            "we", "our", "they", "their", "he", "she", "his", "her",
        }
        return [t for t in tokens if len(t) > 2 and t not in stop_words]
