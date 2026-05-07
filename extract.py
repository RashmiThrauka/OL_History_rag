from pypdf import PdfReader
import os

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    pages_text = []
    
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            pages_text.append({
                "page": page_num + 1,
                "text": text.strip()
            })
    
    return pages_text

# Extract from both books
print("Extracting Grade 10 history book...")
grade10 = extract_text_from_pdf("grade-10-history-text-book-64017cf286c01.pdf")

print("Extracting Grade 11 history book...")
grade11 = extract_text_from_pdf("grade-11-history-text-book-6417fc32c433c.pdf")

# Show results
print(f"\nGrade 10: {len(grade10)} pages extracted")
print(f"Grade 11: {len(grade11)} pages extracted")

# Preview first page of grade 10
print("\n--- PREVIEW: Grade 10, Page 1 ---")
print(grade10[0]["text"][:500])