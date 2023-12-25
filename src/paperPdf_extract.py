import PyPDF2
import re

def extract_text_from_pdf(file_path):
    """
    This function extracts text from a PDF file.
    """
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    pdf_file_obj.close()
    return text


def main():
    """
    The main function that drives the script.
    """
    pdf_dir = "path/to/pdf/dir"

    output = "=========================================================\n"

    for file in os.listdir
    text = extract_text_from_pdf(file_path)
    print(text)

if __name__ == "__main__":
    main()