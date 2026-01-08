import subprocess
from pathlib import Path
from pdf2docx import Converter

def pdf_to_docx(pdf_path, docx_path):
    print("Converting PDF → DOCX...")
    cv = Converter(str(pdf_path))
    cv.convert(str(docx_path))
    cv.close()

def docx_to_epub(docx_path, epub_path):
    print("Converting DOCX → EPUB...")
    subprocess.run([
        "ebook-convert",
        str(docx_path),
        str(epub_path),
        "--enable-heuristics"
    ], check=True)


def pdf_to_epub(pdf_path, epub_path=None, cleanup=True):
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    if epub_path is None:
        epub_path = pdf_path.with_suffix(".epub")
    else:
        epub_path = Path(epub_path)

    docx_path = pdf_path.with_suffix(".docx")

    pdf_to_docx(pdf_path, docx_path)
    docx_to_epub(docx_path, epub_path)

    if cleanup and docx_path.exists():
        docx_path.unlink()

    print(f"\n✅ Successfully created EPUB: {epub_path}")

if __name__ == "__main__":
    pdf_to_epub("100_k8s_interview_questions.pdf")
