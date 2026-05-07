import os
from pathlib import Path

pdf_dir = Path("data/pdfs")

for pdf_file in pdf_dir.glob("*.pdf"):

    modified_time = os.path.getmtime(pdf_file)

    print(pdf_file, modified_time)