import pandas as pd

import datetime
import requests
import io
from pypdf import PdfReader
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

today = datetime.date.today()
formatted_date = today.strftime("%d-%m-%Y")

df = pd.read_excel('medbase.xlsx')

def donwload_pdf_to_text(url):
    # Download the PDF file from the URL
    response = requests.get(url)

    pdf_file = io.BytesIO(response.content)

    # Create a PDF reader object
    #file = PdfReader(pdf_file)

    # Create a PDF resource manager and a text converter
    resource_manager = PDFResourceManager()
    output_stream = io.StringIO()
    converter = TextConverter(resource_manager, output_stream)

    # Create a PDF interpreter object
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    # Process each page in the PDF file
    for page in PDFPage.get_pages(pdf_file):
        page_interpreter.process_page(page)

    # Get the text content of the PDF
    pdf_text = output_stream.getvalue()

    # Close the output stream and the text converter
    output_stream.close()
    converter.close()

    return pdf_text


for index, row in df.iterrows():
    print(row['Nome'])
    url = row['Link']

    donwload_pdf_to_text(url)

    try:
        response = requests.get(url)

    # Create a BytesIO object from the PDF content
    pdf_file = io.BytesIO(response.content)

    # Create a PdfFileReader object
    try:
        pdf_reader = PdfReader(pdf_file)

        # Extract the text from the PDF
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()

        # Write the text to a new text file
        filename = f"{row['Nome']}_{formatted_date}.txt"
        with open(filename, 'w') as f:
            f.write(pdf_text)
        print('success')
    except:
        print('error')
        pass