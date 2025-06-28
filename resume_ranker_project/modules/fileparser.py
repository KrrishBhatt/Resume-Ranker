import os  # interaction with OS
import fitz  # PyMuPDF

# method to extract text from a single pdf at a time
def extract_text_from_pdf(filepath):
    text=""
    with fitz.open(filepath) as doc:
        for page in doc:
            text+=page.get_text()
        return text.strip()

# method to map each file with its text content
# this method returns a dictionary (filename:content)
def extract_texts_from_folder(folder_path):
    texts = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            path = os.path.join(folder_path, filename) # extracting file path
            texts[filename] = extract_text_from_pdf(path)
    return texts 