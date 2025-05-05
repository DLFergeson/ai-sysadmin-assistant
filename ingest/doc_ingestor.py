"""
Handles ingestion of local documents in PDF, DOCX, and TXT formats.
"""

import fitz  # PyMuPDF
from docx import Document
import os

def ingest_local_docs(path):
    """
    Determine file type and process accordingly.

    Args:
        path (str): File path to document.

    Returns:
        str: Extracted text content.
    """
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return _read_pdf(path)
    elif ext == ".docx":
        return _read_docx(path)
    elif ext == ".txt":
        return _read_txt(path)
    else:
        return "Unsupported file type."

def _read_pdf(path):
    """Extract text from each PDF page."""
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

def _read_docx(path):
    """Extract text from Word document."""
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def _read_txt(path):
    """Read plain text file."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
