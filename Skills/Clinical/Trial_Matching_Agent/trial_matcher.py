# COPYRIGHT NOTICE
# This file is part of the "Universal Biomedical Skills" project.
# Copyright (c) 2026 MD BABU MIA, PhD <md.babu.mia@mssm.edu>
# All Rights Reserved.
#
# This code is proprietary and confidential.
# Unauthorized copying of this file, via any medium is strictly prohibited.
#
# Provenance: Authenticated by MD BABU MIA

import json
import argparse
import re

# Try to import advanced libraries, fall back if missing
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

try:
    from sentence_transformers import SentenceTransformer
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False

class Patient:
    def __init__(self, age, gender, conditions, criteria_text=""):
        self.age = age
        self.gender = gender
        self.conditions = conditions  # List of strings
        self.criteria_text = criteria_text # Natural language description

    def __str__(self):
        return f"Patient(Age: {self.age}, Conds: {', '.join(self.conditions)})"

class ClinicalTrial:
    def __init__(self, data):
        self.id = data.get('id')
        self.title = data.get('title')
        self.conditions = data.get('conditions', [])
        self.inclusion = data.get('inclusion_criteria', '')
        self.exclusion = data.get('exclusion_criteria', '')
        self.full_text = f"{self.title} {' '.join(self.conditions)} {self.inclusion} {self.exclusion}"

class TrialMatcher:
    def __init__(self, use_llm=False):
        self.use_llm = use_llm and HAS_TRANSFORMERS
        if self.use_llm:
            print("Loading Sentence Transformer model (all-MiniLM-L6-v2)...")
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        elif use_llm and not HAS_TRANSFORMERS:
            print("Warning: 'sentence_transformers' not found. Falling back to keyword matching.")
        
    def _tokenize(self, text):
        return set(re.findall(r'\w+', text.lower()))

    def _keyword_score(self, patient_text, trial_text):
        # Jaccard Similarity of tokens
        p_tokens = self._tokenize(patient_text)
        t_tokens = self._tokenize(trial_text)
        
        if not p_tokens or not t_tokens:
            return 0.0
            
        intersection = p_tokens.intersection(t_tokens)
        union = p_tokens.union(t_tokens)
        return len(intersection) / len(union)

    def _semantic_score(self, patient_text, trial_text):
        if not self.use_llm:
            return 0.0
        embeddings = self.model.encode([patient_text, trial_text])
        # Cosine similarity
        a = embeddings[0]
        b = embeddings[1]
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def match(self, patient, trials):
        results = []
        
        # Construct a query string for the patient
        patient_query = f"{ ' '.join(patient.conditions)} {patient.criteria_text}"
        
        for trial in trials:
            # 1. Hard Filter: Age (Simple regex parsing for demonstration)
            # This is a basic example; real extraction is complex
            min_age_match = re.search(r'Age >=? (\d+)', trial.inclusion)
            if min_age_match:
                min_age = int(min_age_match.group(1))
                if patient.age < min_age:
                    continue # Skip this trial

            # 2. Score
            if self.use_llm:
                score = self._semantic_score(patient_query, trial.full_text)
                method = "Semantic"
            else:
                score = self._keyword_score(patient_query, trial.full_text)
                method = "Keyword"
            
            # Boost score if condition matches exactly
            for cond in patient.conditions:
                if any(cond.lower() in t_cond.lower() for t_cond in trial.conditions):
                    score += 0.3
                    break
            
            results.append({
                "trial_id": trial.id,
                "title": trial.title,
                "score": score,
                "method": method
            })
            
        # Sort by score descending
        results.sort(key=lambda x: x['score'], reverse=True)
        return results

def main():
    parser = argparse.ArgumentParser(description="TrialGPT - Clinical Trial Matching Agent")
    parser.add_argument("--trials", default="dummy_data.json", help="Path to trials JSON")
    parser.add_argument("--age", type=int, required=True, help="Patient Age")
    parser.add_argument("--condition", required=True, help="Patient Condition (primary)")
    parser.add_argument("--notes", default="", help="Additional patient notes")
    parser.add_argument("--use-llm", action="store_true", help="Use LLM embeddings if available")
    
    args = parser.parse_args()
    
    # Load Trials
    try:
        with open(args.trials, 'r') as f:
            trials_data = json.load(f)
        trials = [ClinicalTrial(t) for t in trials_data]
    except FileNotFoundError:
        print(f"Error: Trials file '{args.trials}' not found.")
        return

    # Create Patient
    patient = Patient(args.age, "Unknown", [args.condition], args.notes)
    
    print(f"Matching trials for: {patient}...")
    
    matcher = TrialMatcher(use_llm=args.use_llm)
    matches = matcher.match(patient, trials)
    
    print(f"\nFound {len(matches)} potential matches:\n")
    print(f"{'ID':<10} {'Score':<10} {'Title'}")
    print("-" * 60)
    for m in matches:
        print(f"{m['trial_id']:<10} {m['score']:.4f}     {m['title']}")

if __name__ == "__main__":
    main()

__AUTHOR_SIGNATURE__ = "9a7f3c2e-MD-BABU-MIA-2026-MSSM-SECURE"
