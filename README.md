# Rolevant
AI-powered career discovery platform that maps your skills to roles 
across multiple industries — and tells you exactly what's missing.

---

## Versions

### V1 — Foundation
- PDF resume extraction with text cleaning
- Semantic matching using sentence embeddings (all-MiniLM-L6-v2)
- Keyword gap analysis
- Hardcoded role profiles for 6 industries

### V2 — Data-Driven (current)
- 47 roles extracted from 7,473 real LinkedIn job postings (2023-2024)
- Precomputed role embeddings stored in JSON for faster inference
- Expanded industry coverage across tech, finance, healthcare, HR, sales, legal and more

### V3 — Planned
- NER-based skill extraction for cleaner, more precise role embeddings
- FastAPI backend for production deployment
