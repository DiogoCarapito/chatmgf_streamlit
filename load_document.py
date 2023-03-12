from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

file = 'data/Programa-Nacional-Vigilancia-Gravidez-Baixo-Risco-2015.pdf'
#file = OnlinePDFLoader('http://nocs.pt/wp-content/uploads/2016/01/Programa-Nacional-Vigilancia-Gravidez-Baixo-Risco-2015.pdf')
loader = UnstructuredPDFLoader(file)

data = loader.load()

print (f'You have {len(data)} document(s) in your data')
print (f'There are {len(data[0].page_content)} characters in your document')

'''import os
import openai
openai_api_key = os.environ.get('OPENAI_API_KEY')'''

