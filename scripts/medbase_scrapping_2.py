# scrapping text form a pdf online
import datetime
import requests
import io
import re
import csv
import pandas as pd

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


# get today's date
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

    try:
        pdf_text = donwload_pdf_to_text(url)

        filename = f"scrapped_data/{row['Nome']}_{formatted_date}.txt"
        with open(filename, 'w') as f:
            f.write(pdf_text)

        print('scuccess')

    except:
        print('error')
        pass