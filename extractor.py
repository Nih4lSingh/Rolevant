import fitz
import re
 
def extract_text_pdf(pdf_path):
    doc=fitz.open(pdf_path)
    all_text=""
    for page in doc:
        text=page.get_text()
        all_text+=text
    clean=re.sub(r'[^\x00-\x7F,]+',' ',all_text)
    ' '.join(clean.split())
    return clean
