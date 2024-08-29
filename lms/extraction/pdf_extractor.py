from unstructured.partition.auto import partition
from unstructured.documents.elements import (
    Table, Text, Title, NarrativeText, ListItem, PageBreak, Header
)
from unstructured.partition.pdf import partition_pdf
import os

def extract_pdf_content(input:str, pdf_path:str, strategy='ocr_only'):
    pdf_path = os.path.join(input, pdf_path)
    if strategy not in ['ocr_only', 'high_res']:
        raise ValueError("Strategy must be either 'ocr_only' or 'high_res'")

    if strategy == 'ocr_only':
        elements = partition(
            filename=pdf_path,
            strategy="ocr_only",
            languages=['eng'], 
        )
    else:
        ocr_config = {
            'languages': ['eng'],
            'strategy': 'hi_res',
            'detection_model': 'yolox',
            'extract_images_in_pdf': True,
        }
        elements = partition_pdf(filename=pdf_path, **ocr_config)
    

    content = []

    # print("Element details with metadata:")
    
    for element in elements:
        
        # print(f"Element Text: {element.text}")
        # metadata = element.metadata
        # metadata_details = {attr: getattr(metadata, attr, None) for attr in dir(metadata) if not attr.startswith('_')}
        # print(f"Metadata: {metadata_details}")

        if isinstance(element, Table):
            content.append(f"[TABLE]\n{element.text}\n[/TABLE]")
        elif isinstance(element, (Text, Title, NarrativeText, ListItem, Header)):
            content.append(element.text)
        elif isinstance(element, PageBreak):
            content.append("\n--- Page Break ---\n")

    return "\n".join(content)