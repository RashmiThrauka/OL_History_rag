from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

# Use Grok-compatible embeddings via OpenAI client
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    openai_api_base=os.getenv("BASE_URL")
)

def extract_text_from_pdf(pdf_path, grade_label):
    reader = PdfReader(pdf_path)
    pages_text = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages_text.append({
                "text": text.strip(),
                "page": page_num + 1,
                "grade": grade_label
            })
    return pages_text

def chunk_pages(pages_text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = []
    metadatas = []
    for page in pages_text:
        split_texts = splitter.split_text(page["text"])
        for chunk in split_texts:
            chunks.append(chunk)
            metadatas.append({
                "page": page["page"],
                "grade": page["grade"]
            })
    return chunks, metadatas

# Extract text
print("Extracting text from PDFs...")
grade10_pages = extract_text_from_pdf(
    "grade-10-history-text-book-64017cf286c01.pdf", "Grade 10")
grade11_pages = extract_text_from_pdf(
    "grade-11-history-text-book-6417fc32c433c.pdf", "Grade 11")

all_pages = grade10_pages + grade11_pages
print(f"Total pages: {len(all_pages)}")

# Chunk the text
print("Chunking text...")
chunks, metadatas = chunk_pages(all_pages)
print(f"Total chunks created: {len(chunks)}")

# Create embeddings and store in ChromaDB
print("Creating embeddings and storing in ChromaDB...")
print("This will take a few minutes...")

vectorstore = Chroma.from_texts(
    texts=chunks,
    embedding=embeddings,
    metadatas=metadatas,
    persist_directory="./chroma_db"
)

print("\nDone! Your knowledge base is ready.")
print(f"Total chunks stored: {len(chunks)}")