import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

# Open the PDF file in binary mode
with open('example.pdf', 'rb') as file:
    # Create a PDF resource manager and a text converter
    resource_manager = PDFResourceManager()
    output_stream = io.StringIO()
    converter = TextConverter(resource_manager, output_stream)

    # Create a PDF interpreter object
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    # Process each page in the PDF file
    for page in PDFPage.get_pages(file):
        page_interpreter.process_page(page)

    # Get the text content of the PDF
    pdf_text = output_stream.getvalue()

    # Close the output stream and the text converter
    output_stream.close()
    converter.close()

# Print the text content
print(pdf_text)
