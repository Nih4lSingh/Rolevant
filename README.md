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
- Semantic matching using sentence embeddings (all-MiniLM-L6-v2)
- Keyword gap analysis
- Hardcoded role profiles for 6 industries

### V1 structure
.

├── README.md          # Project documentation

├── app.py             # Main Streamlit application

├── extractor.py       # Text extractor logic

├── matcher.py         # Matching and scoring logic

├── requirements.txt   # Project dependencies

└── roles.py           # Hardcoded keywords for 6 roles

### Basic UI
<img width="2430" height="1402" alt="image" src="https://github.com/user-attachments/assets/747496c4-c199-4a9d-8eaa-5dda3641c71e" />
### 6 role options
<img width="1556" height="874" alt="image" src="https://github.com/user-attachments/assets/75e7fd12-0d54-4d5d-b143-7e93d39fc5df" />
### missing keywords and top 5 suggestions
<img width="1516" height="1364" alt="image" src="https://github.com/user-attachments/assets/bd1fdf88-6c1b-409e-90b7-aa5ba6c85832" />

### V2 — Data-Driven (current)
- 47 roles extracted from 7,473 real LinkedIn job postings (2023-2024)
- Semantic matching using sentence embeddings (all-mpnet-base-v2)
- Precomputed role embeddings stored in JSON for faster inference
- Expanded industry coverage across tech, finance, healthcare, HR, sales, legal and more

### V2 structure
.

├── README.md             # Project documentation

├── app.py                # Main Streamlit application

├── extractor.py          # Text extractor logic

├── matcher.py            # Matching and scoring logic

├── preprocessing.ipynb   # Data preprocessing pipeline

├── requirements.txt      # Project dependencies

└── role_data.json        # Precomputed embeddings and keywords for 47 roles


### 47 role options
<img width="2422" height="1382" alt="image" src="https://github.com/user-attachments/assets/76bc6330-2ce8-45bb-9690-4bc1e9451700" />
### missing keywords and top 5 suggestions
<img width="2348" height="1384" alt="image" src="https://github.com/user-attachments/assets/2d340604-dff7-42f6-8e15-89716c0ec8ef" />



### How are role profiles built?
Role embeddings are precomputed from 7,473 real LinkedIn job postings 
across 47 roles using sentence-transformers (all-mpnet-base-v2). 
See preprocessing/preprocessing.ipynb for the full pipeline.

### V3 — Planned
- NER-based skill extraction for cleaner, more precise role embeddings
- FastAPI backend for production deployment
