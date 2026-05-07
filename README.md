# O/L History RAG — Sri Lanka Government School Textbook Q&A

A Retrieval-Augmented Generation (RAG) application that allows students and teachers to ask natural language questions about Sri Lankan Grade 10 and Grade 11 history curriculum — and receive accurate, cited answers directly from the official textbooks.

---

## Problem This Solves

Students and teachers waste hours manually searching through 300+ pages of history textbooks to verify facts, clarify doubts, or confirm MCQ answers. This tool answers any curriculum question in seconds and tells you exactly which page the answer came from.

Built with real Grade 10 and Grade 11 English medium history textbooks published by Sri Lanka's Educational Publications Department.

---

## Architecture
PDF Textbooks → Text Extraction → Chunking → Embeddings → ChromaDB
↓
User Question → Embed Query → Retrieve Top-5 Chunks → LLM → Cited Answer

---

## Tech Stack

| Component | Tool |
|---|---|
| PDF Parsing | PyPDF |
| Text Chunking | LangChain RecursiveCharacterTextSplitter |
| Embeddings | OpenAI text-embedding-3-small |
| Vector Store | ChromaDB |
| LLM | GPT-4o-mini |
| Frontend | Streamlit |

---

## Limitations

- Handles text-based queries only — image and map-based MCQs are out of scope for this version
- Answers are grounded in textbook content only — no outside knowledge
- English medium textbooks only

---

## Roadmap

- [x] PDF text extraction
- [x] Text chunking pipeline
- [ ] ChromaDB vector store setup
- [ ] Q&A with citations
- [ ] Streamlit interface
- [ ] Evaluation on 20 question test set
- [ ] Deploy to Streamlit Community Cloud

---
