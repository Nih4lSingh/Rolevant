# Rolevant — Project Timeline

A version-by-version breakdown of how Rolevant evolved from a prototype to a data-driven career discovery platform.

---

## V1 — Foundation

**Initial Features:**
- PDF resume extraction with text cleaning
- Semantic matching using sentence embeddings (`all-MiniLM-L6-v2`)
- Keyword gap analysis
- Hardcoded role profiles for 6 industries

**Tech Stack**

| Layer | Tool |
|---|---|
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) |
| Similarity | scikit-learn cosine similarity |
| Keywords | Hardcoded keyword strings |
| PDF Parsing | PyMuPDF |
| UI | Streamlit |

**Project Structure**
```
.
├── README.md          # Project documentation
├── app.py             # Main Streamlit application
├── extractor.py       # PDF text extraction logic
├── matcher.py         # Matching and scoring logic
├── requirements.txt   # Project dependencies
└── roles.py           # Hardcoded keywords for 6 roles
```

**Screenshots**

Basic UI

<img width="2430" height="1402" alt="image" src="https://github.com/user-attachments/assets/747496c4-c199-4a9d-8eaa-5dda3641c71e" />

6 role options

<img width="1556" height="874" alt="image" src="https://github.com/user-attachments/assets/75e7fd12-0d54-4d5d-b143-7e93d39fc5df" />

Missing keywords and top 5 suggestions

<img width="1516" height="1364" alt="image" src="https://github.com/user-attachments/assets/bd1fdf88-6c1b-409e-90b7-aa5ba6c85832" />

---

## V2 — Data-Driven

**What changed:**
- 47 roles extracted from 7,473 real LinkedIn job postings (2023–2024)
- Upgraded to `all-mpnet-base-v2` for better semantic understanding
- Precomputed role embeddings stored in JSON for faster inference
- Expanded industry coverage across tech, finance, healthcare, HR, sales, legal and more
- Keywords extracted using TF-IDF with n-gram support

**Tech Stack**

| Layer | Tool |
|---|---|
| Embeddings | sentence-transformers (`all-mpnet-base-v2`) |
| Similarity | scikit-learn cosine similarity |
| Keywords | TF-IDF (scikit-learn) |
| PDF Parsing | PyMuPDF |
| UI | Streamlit |
| Data | LinkedIn Job Postings 2023–2024 (Kaggle) |

**How are role profiles built?**

Role embeddings are precomputed from 7,473 real LinkedIn job postings across 47 roles using sentence-transformers (`all-mpnet-base-v2`). See `preprocessing.ipynb` for the full pipeline.

**Project Structure**
```
.
├── README.md               # Project documentation
├── app.py                  # Main Streamlit application
├── extractor.py            # PDF text extraction logic
├── matcher.py              # Matching and scoring logic
├── preprocessing.ipynb     # Data preprocessing pipeline
├── requirements.txt        # Project dependencies
└── role_data.json          # Precomputed embeddings and keywords for 47 roles
```

**Screenshots**

47 role options

<img width="2422" height="1382" alt="image" src="https://github.com/user-attachments/assets/76bc6330-2ce8-45bb-9690-4bc1e9451700" />

Missing keywords and top 5 suggestions

<img width="2348" height="1384" alt="image" src="https://github.com/user-attachments/assets/2d340604-dff7-42f6-8e15-89716c0ec8ef" />

---

## V3 — NER + LLM Validation *(current)*

**What changed:**
- Replaced TF-IDF keyword extraction with NER-based skill extraction using `algiraldohe/lm-ner-linkedin-skills-recognition`
- Added LLM validation via Groq API (LLaMA 3.3 70B) to remove noise and semantic duplicates
- Sentence-level averaged embeddings for more representative role vectors
- Keywords now represent actual skills, not frequent words

**Tech Stack**

| Layer | Tool |
|---|---|
| Embeddings | sentence-transformers (`all-mpnet-base-v2`) |
| Similarity | scikit-learn cosine similarity |
| Skill Extraction | NER (`algiraldohe/lm-ner-linkedin-skills-recognition`) |
| LLM Validation | Groq API (LLaMA 3.3 70B) |
| PDF Parsing | PyMuPDF |
| UI | Streamlit |
| Data | LinkedIn Job Postings 2023–2024 (Kaggle) |

**How are role profiles built?**

Skills are extracted from 7,473 real LinkedIn job postings using a LinkedIn-trained NER model. Extracted skills are frequency filtered then validated by LLaMA 3.3 70B via Groq API to remove noise, company names, and semantic duplicates. Role embeddings are computed by averaging sentence-level embeddings using `all-mpnet-base-v2`.

**Project Structure**
```
.
├── README.md                  # Project documentation
├── TIMELINE.md                # Version history
├── app.py                     # Main Streamlit application
├── extractor.py               # PDF text extraction logic
├── matcher.py                 # Matching and scoring logic
├── preprocessing.ipynb        # Data preprocessing pipeline (v2 + v3)
├── requirements.txt           # Project dependencies
└── role_data.json             # Precomputed embeddings and keywords for 47 roles
```

---

## V4 — Planned

- FastAPI backend for production deployment
- React frontend for a more polished user experience
- Expanded role coverage using additional datasets
