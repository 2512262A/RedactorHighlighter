# RedactorHighlighter

AI-powered app that detects and redacts or highlights information (names, locations, organizations) from documents using BERT-based NER.

---

## Features

- Upload files: TXT, DOCX, PDF  
- Named Entity Recognition (Indonesian BERT)  
- Redaction of PER / LOC / ORG  
- Highlight or redacted output  
- Download processed file  

---

## Tech Stack

- Streamlit  
- Hugging Face Transformers  
- PyTorch  

---

## Example

![Example Output](https://kappa.lol/6pLPRH)

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/2512262A/RedactorHighlighter.git

# move to the repo directory
cd RedactorHighlighter

#install all the requirements
pip install -r requirements.txt

# Run the app with streamlit
streamlit run app.py
```
---

## Weakness

it didnt work quite well with text that has english word in it

---

## Future Works

* OCR for PDF files
* Fine-Tune the BERT model
* Consistent annomyzation to preserved identity across the document

---
