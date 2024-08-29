import argparse
from lms.extraction.pdf_extractor import extract_pdf_content
from lms.file_tester.pdf_file_test import test_file
import sys
def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF files")
    parser.add_argument("-n", "--file-name", help="Enter the name of the file to extract data")
    parser.add_argument("-s", "--stratergy", choices=["hi_res", "ocr_only"], help="Enter the name of the file to extract data")
    parser.add_argument("-i",  "--input", help="Enter the directory containing PDF for extractions")
    parser.add_argument("-o",  "--output", help="Path to outputfile")
    args = parser.parse_args()
    try:
        test_file(args.file_name)
        content = extract_pdf_content(input=args.input, pdf_path=args.file_name, strategy=args.stratergy)
        print("Extracted Content:")
        print(content)

        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Content has been saved to 'extracted_content.txt'")
    except Exception as e:
        print(f"An error occurred while processing the PDF: {str(e)}")
        sys.exit(1)
    


if __name__ == "__main__":
    main()