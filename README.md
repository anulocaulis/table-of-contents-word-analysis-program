# DSA Group Project — Text Analysis & TOC Tree

**Course:** DTSC 5501 - Data Structures and Algorithms  
**Team:**
| Name | Role |
|------|------|
| Mike Beitner | Tree Architect — Q1 TOC Tree |
| Christopher Taylor | Text Analyst — Q2 Preprocessing, Frequency Analysis & N-grams |
| Luis Echeverry | Viz & Integration Lead — Q2 Charts, Big-O Analysis & QA |

---

## Project Overview

**Q1 — Table of Contents Tree**  
Builds a hierarchical tree from a DS/AI/ML book's Table of Contents using
pure Python. Implements `insert()`, `print_toc()` in three modes, `depth()`,
and `height()`.

**Q2 — Text Analysis**  
Analyzes a public-domain novel from Project Gutenberg across two workstreams:
- Christopher Taylor: preprocessing pipeline, letter/word frequency, bigrams,
  trigrams, and sentence metrics
- Luis Echeverry: all visualizations, Big-O writeup, and final integration

---

## Workload Breakdown

### Mike Beitner — Tree Structure and Hierarchical Design
- Select a technical data science book and document the source URL
- Define the primary tree node classes and the book orchestration class
- Develop the recursive insertion function for chapter and subchapter paths
- Implement preorder traversal logic to display the table of contents
- Create the numbering logic for the indented table of contents output
- Write methods to calculate node depth and total tree height

### Christopher Taylor — Text Preprocessing and Word Frequency Analysis
- Select a public domain novel and document the source via Project Gutenberg
- Create a cleaning pipeline for lowercase conversion and punctuation removal
- Implement tokenization logic and integrate the allowed stopword list
- Generate frequency counts for individual letters and the top 40 words
- Calculate bigram and trigram sequences using a sliding window approach
- Compute sentence structure metrics including average word count and length distribution

### Luis Echeverry — Visualization, Complexity Analysis, and Quality Assurance
- Produce bar charts and tables for letter and word frequency distributions
- Generate word clouds for unigrams, bigrams, and trigrams using Matplotlib
- Produce sentence length distribution histogram from Christopher Taylor's computed data
- Conduct Big-O complexity analysis for all preprocessing and search algorithms
- Draft the final report notebook with explanations of design choices and results
- Set up the testing suite using assertions to validate core function outputs
- Organize the README and verify the notebook executes start to finish

---

## Data Sources

| Item | Source |
|------|--------|
| Q1 Textbook | *Math for Deep Learning - Ronald T.Kneusel* |
| Q2 URL | (https://a.co/d/02MiYbto) |
| Q2 Novel | *The Brothers Karamazov* — Fyodor Dostoevsky (tr. Constance Garnett) |
| Q2 URL | (https://www.gutenberg.org/files/28054/28054-0.txt) |

---

## Setup Instructions

### Option A — Google Colab (recommended)
1. Open the relevant notebook in [Google Colab](https://colab.research.google.com/)
2. Run **Runtime → Restart and Run All**
3. No manual setup required — Cell 1 handles all installs and downloads

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

> **No NLP libraries** (spaCy, gensim, etc.) and **no tree libraries** permitted.  
> Q1 uses **core Python only** — no external packages whatsoever.

---

## Notebook Cell Map — Q2

| Cell | Owner | Description |
|------|-------|-------------|
| 1 | Setup | Install packages, download NLTK stopwords |
| 2 | Setup | All imports |
| 3 | P2 | Download novel, `loadGutenText()` |
| 4 | P2 | Preprocessing pipeline — `toLower`, `removePunctuation`, `tokenize`, `removeStopwords`, `preprocess` |
| 5 | P2 | Unit tests — `runPreprocTests()` |
| 6 | P2 | Letter frequency table — `computeLetterFreqs()` |
| 7 | P3 | Letter frequency bar chart |
| 8 | P2 | Word frequency table — `computeWordFreqs()` |
| 9 | P3 | Word frequency bar chart |
| 10 | P3 | Word cloud — unigrams |
| 11 | P3 | Big-O analysis & letter distribution interpretation |
| 12 | P2 | Bigram counts — `computeBigrams()` |
| 13 | P2 | Trigram counts — `computeTrigrams()` |
| 14 | P2 | Sentence metrics — `computeSentenceMetrics()` |
| 15+ | P3 | Bigram/trigram word clouds, sentence histogram, final report |

---

## Key Results

- Most frequent letter: **e** *(11.942%)*
- Top word (post-stopword removal): **one**
- Most common bigram: **fyodr pavlovitch**
- Most common trigram: **father pa ssy**
- Average words per sentence: **14.54**
---

## Branch Strategy

| Branch | Owner | Purpose |
|--------|-------|---------|
| `main` | All | Always runnable — PRs only, no direct pushes |
| `q1/toc-tree` | Mike Beitner | Q1 notebook |
| `q2/preprocessing` | Christopher Taylor | Cells 3–6 |
| `q2/ngrams-sentences` | Christopher Taylor | Cells 12–14 |
| `q2/viz-integration` | Luis Echeverry | Cells 7, 9–11, 15+ |
