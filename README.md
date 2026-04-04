# DSA Group Project — Text Analysis & TOC Tree

**Course:** Graduate Data Structures and Algorithms  
**Team:**
| Name | Role |
|------|------|
| Mike Beitner | Tree Architect — Q1 TOC Tree |
| Christopher Taylor | Text Analyst — Q2 Preprocessing & Frequency Analysis |
| Luis Echeverry | Viz & Integration Lead — Q2 N-grams, Challenge, Notebook Assembly |

---

## Project Overview

This project has two deliverables:

**Q1 — Table of Contents Tree (45 pts)**  
Builds a hierarchical tree from a DS/AI/ML book's Table of Contents using pure Python. Implements `insert()`, `print_toc()` in three modes, `depth()`, and `height()`.

**Q2 — Text Analysis (45 pts)**  
Analyzes a public-domain novel from Project Gutenberg. Covers full preprocessing, letter frequency, word frequency, bigrams, trigrams, and sentence-level metrics.

---

## Data Sources

| Item | Source |
|------|--------|
| Q1 Book | *(Person 1 to fill in — title + URL)* |
| Q2 Novel | *The Brothers Karamazov* — Fyodor Dostoevsky (tr. Constance Garnett) |
| Q2 URL | https://www.gutenberg.org/files/28054/28054-0.txt |

---

## Setup Instructions

### Option A — Google Colab (recommended)
1. Open the notebook in [Google Colab](https://colab.research.google.com/)
2. Run **Runtime → Restart and Run All**
3. No manual setup required — Cell 1 handles all installs

### Option B — Run locally
```bash
# Clone the repo
git clone https://github.com/<your-org>/DSA-Group-Project.git
cd DSA-Group-Project

# Install dependencies
pip install -r requirements.txt

# Download NLTK stopwords
python -c "import nltk; nltk.download('stopwords')"

# Launch Jupyter
jupyter notebook Q1/DSA_Group_Project_1.ipynb
jupyter notebook Q2/DSA_Group_Project_2.ipynb
```

---

## Allowed Libraries

| Library | Purpose |
|---------|---------|
| `re` | Text cleaning via regex |
| `string` | Alphabet constants |
| `math` | Mathematical utilities |
| `collections` / `Counter` | Frequency counting |
| `itertools` | N-gram generation |
| `pandas` | Tabular display |
| `matplotlib` | Charts and plots |
| `wordcloud` | Word cloud visualization |
| `nltk` | Stopword list **only** |

> **No NLP libraries** (spaCy, gensim, etc.) and **no tree libraries** are permitted.

---

## Key Results

*(To be filled in after final run)*
- Most frequent letter: **?** (?%)
- Top word (post-stopword removal): **?**
- Most common bigram: **?**
- Most common trigram: **?**
- Average words per sentence: **?**
