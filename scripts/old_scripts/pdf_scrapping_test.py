import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
import requests
#from pypdf import PdfReader

#pdf= 'Consenso-Nacional-Menopausa-2021.pdf'

pdf_url = 'https://ordemdosmedicos.pt/wp-content/uploads/2017/09/ZRecomendacoes_merged_19_12_2022.pdf'

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

# Print the text content
print(donwload_pdf_to_text(pdf_url))
