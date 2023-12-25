import PyPDF2
import os
import argparse

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file.
    
    :param file_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    with open(file_path, 'rb') as pdf_file_obj:
        pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # Ensures that None is not added if text extraction fails
    return text

def main(pdf_dir, output_path):
    """
    Main function to extract text from all PDF files in a directory.
    
    :param pdf_dir: Directory containing PDF files.
    :param output_path: Path to save the output text file.
    """
    all_text = ""
    for file_name in os.listdir(pdf_dir):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(pdf_dir, file_name)
            print(f"Processing {file_name}...")
            text = extract_text_from_pdf(file_path)
            all_text += f"\nFile: {file_name}\n{text}\n"
            all_text += "=========================================================\n"

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(all_text)
    print(f"Extraction complete. Text saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract text from PDF files in a directory")
    parser.add_argument("pdf_dir", help="Path to the directory containing PDF files")
    parser.add_argument("output_path", help="Path where the extracted text will be saved")
    
    args = parser.parse_args()
    main(args.pdf_dir, args.output_path)
