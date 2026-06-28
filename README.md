# Rolevant
AI-powered career discovery platform that maps your skills to roles 
across multiple industries — and tells you exactly what's missing.

---
## How it works
Rolevant extracts text from your uploaded PDF resume, converts it into 
a semantic embedding using sentence-transformers, and compares it against 
precomputed embeddings for 47 roles built from real LinkedIn job postings. 
Cosine similarity produces a match score, and TF-IDF keyword analysis 
identifies exactly which skills are missing for each role.
---
## Versions

### V1 — Foundation
- PDF resume extraction with text cleaning
- Semantic matching using sentence embeddings (all-mpnet-base-v2)
- Keyword gap analysis
- Hardcoded role profiles for 6 industries

### V2 — Data-Driven (current)
- 47 roles extracted from 7,473 real LinkedIn job postings (2023-2024)
- Precomputed role embeddings stored in JSON for faster inference
- Expanded industry coverage across tech, finance, healthcare, HR, sales, legal and more

### How are role profiles built?
Role embeddings are precomputed from 7,473 real LinkedIn job postings 
across 47 roles using sentence-transformers (all-mpnet-base-v2). 
See preprocessing/preprocessing.ipynb for the full pipeline.

### V3 — Planned
- NER-based skill extraction for cleaner, more precise role embeddings
- FastAPI backend for production deployment
