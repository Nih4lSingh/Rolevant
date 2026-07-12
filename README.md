# Rolevant

> AI-powered career discovery platform that maps your skills to roles across multiple industries — and tells you exactly what companies look for.

**🔗 Live Demo:** [https://rolevant.streamlit.app/](https://rolevant.streamlit.app/)

---

## What is Rolevant?

Rolevant reads your resume and tells you two things:

1. **Which roles suit you best** — ranked across 47 roles spanning tech, finance, healthcare, HR, sales, legal, and more
2. **What skills companies look for** — so you know exactly what to learn next

---

## How It Works

1. Upload your resume as a PDF
2. Optionally select a specific role to check your fit
3. Click **Evaluate**
4. Get a semantic match score, top 5 recommended roles, and a list of skills companies commonly look for

Rolevant extracts text from your resume, converts it into a semantic embedding using `sentence-transformers`, and compares it against precomputed role embeddings built from 7,473 real LinkedIn job postings. A normalized cosine similarity produces the match score, and NER-based skill extraction — validated with an LLM — identifies relevant skills per role.

---

## Tech Stack

| Layer | Tool |
|---|---|
| Embeddings | sentence-transformers (`all-mpnet-base-v2`) |
| Similarity | scikit-learn cosine similarity (normalized) |
| Skill Extraction | NER (`algiraldohe/lm-ner-linkedin-skills-recognition`) |
| LLM Validation | Groq API (LLaMA 3.3 70B) |
| PDF Parsing | PyMuPDF |
| UI | Streamlit |
| Data | LinkedIn Job Postings 2023–2024 (Kaggle) |

---

## How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/your-username/rolevant.git
cd rolevant
```

**2. Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
streamlit run app.py
```

**5. Open in browser**
```
http://localhost:8501
```

---

## Industries Covered

| Industry | Example Roles |
|---|---|
| Tech | ML Engineer, Software Engineer, Data Scientist, DevOps Engineer |
| Finance | Financial Analyst, Accountant, Tax Manager, Financial Advisor |
| Healthcare | Registered Nurse, Physician Assistant, Physical Therapist |
| HR | HR Manager, HR Generalist, Recruiter |
| Sales | Sales Manager, Account Executive, Business Development Manager |
| Legal | Attorney, Paralegal |
| Marketing | Marketing Manager, Marketing Coordinator, Graphic Designer |
| Management | Project Manager, Product Manager, Operations Manager |

---

## Limitations

- Optimized for common roles — highly specialized domains (semiconductor, aerospace) may show lower accuracy
- Resume must be in PDF format
- Results are based on LinkedIn job postings from 2023–2024

---

## Version History

See [TIMELINE.md](TIMELINE.md) for a full breakdown of how Rolevant evolved across versions.