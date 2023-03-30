# scrapping text form a pdf online
import datetime
import requests
import io
import re
import csv

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

# get today's date
today = datetime.date.today()
formatted_date = today.strftime("%d-%m-%Y")

# url of the pdf
url = 'https://ordemdosmedicos.pt/wp-content/uploads/2017/09/ZRecomendacoes_merged_19_12_2022.pdf'

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

text_from_pdf = donwload_pdf_to_text(url)

# Replace the text
replacements = {
    '   Justificação   ': ' Justificação: ',
}
text_processed = text_from_pdf
for old, new in replacements.items():
    text_processed = text_processed.replace(old, new)

#print(text_from_pdf)

# Find all the matches of the pattern
pattern = r'Recomendação   (Escolha.*?)  A informação apresentada'
#sliced_text = re.findall(pattern, text_from_pdf, flags=re.UNICODE)
sliced_text = re.findall(pattern, text_processed)

#print(sliced_text)

# Save the text content to a csv file
with open('scrapped_data/Recomendações_choosing_wisely_'+formatted_date+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Recomendação'])
    for i, string in enumerate(sliced_text):
        writer.writerow([i, string])