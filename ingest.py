from pypdf import PdfReader
from pathlib import Path
import json

DATA = []


# ---------------------------------
# TEXT CHUNKING
# ---------------------------------

def chunk_text(text, chunk_size=500, overlap=100):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# ---------------------------------
# PDF INGESTION
# ---------------------------------

pdf_dir = Path("data/pdfs")

for pdf_file in pdf_dir.glob("*.pdf"):

    try:

        reader = PdfReader(str(pdf_file))

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        chunks = chunk_text(text)

        for idx, chunk in enumerate(chunks):

            DATA.append({
                "source": str(pdf_file),
                "type": "pdf",
                "chunk_id": idx,
                "filename": pdf_file.name,
                "folder": "pdfs",
                "content": chunk
            })

        print(f"[PDF] Processed: {pdf_file}")

    except Exception as e:
        print(f"[PDF ERROR] {pdf_file} -> {e}")


# ---------------------------------
# CODE INGESTION
# ---------------------------------

repo_dir = Path("data/repos/langchain")

TARGET_FOLDERS = [
    "chains",
    "retrievers",
    "vectorstores"
]

for folder in TARGET_FOLDERS:

    target_path = repo_dir / "libs" / "langchain" / "langchain" / folder

    if not target_path.exists():
        print(f"[WARNING] Missing folder: {target_path}")
        continue

    for file in target_path.rglob("*.py"):

        try:

            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            chunks = chunk_text(content)

            for idx, chunk in enumerate(chunks):

                DATA.append({
                    "source": str(file),
                    "type": "code",
                    "chunk_id": idx,
                    "filename": file.name,
                    "folder": folder,
                    "content": chunk
                })

            print(f"[CODE] Processed: {file}")

        except Exception as e:
            print(f"[CODE ERROR] {file} -> {e}")


# ---------------------------------
# SAVE OUTPUT
# ---------------------------------

processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)

output_file = processed_dir / "documents.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(DATA, f, indent=2, ensure_ascii=False)


print("\n===================================")
print(f"Total chunks processed: {len(DATA)}")
print(f"Saved to: {output_file}")
print("===================================")