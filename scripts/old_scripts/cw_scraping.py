# scrapping text form a pdf online
import datetime
import requests
import io
import re
import csv
import collections
from pypdf import PdfReader
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

today = datetime.date.today()
formatted_date = today.strftime("%d-%m-%Y")

url = 'https://ordemdosmedicos.pt/wp-content/uploads/2017/09/ZRecomendacoes_merged_19_12_2022.pdf'

# Download the PDF file from the URL
response = requests.get(url)

pdf_file = io.BytesIO(response.content)

# Create a PDF reader object
pdf_reader = PdfReader(pdf_file)

# Get the text content of the PDF
pdf_text = ""
for page in pdf_reader.pages:
    pdf_text += page.extract_text()

# Print the text content
#print(pdf_text)
#print('##########\n')

replacements = {
    ''' página 1 de 1  
Choosing Wisely  Portugal  
Escolhas Criteriosas em Saúde ''': '',
    ''' página 1 de 2  
Choosing Wisely  Portugal  
Escolhas Criteriosas em Saúde ''': '',
    ''' página 2 de 2  
Choosing Wisely  Portugal  
Escolhas Criteriosas em Saúde ''': '',
    'n ão': 'não',
    '-\n': '',
    '\n': ' ',
    '  ': ' ',
    '   ': ' ',
    '    ': ' ',
    '     ': ' ',
    '      ': ' ',
    '       ': ' ',
    '        ': ' ',
    ' -': '-',
    ' . ': '. ',
    ' , ': ', ',
    '.  ': '. ',
    ':  ': ': ',
    'Justificação ': 'Justificação: ',
    ' pa ra ': ' para ',
    ' sup orte': ' suporte',
    ' a ntes': ' antes',
    'Bibliogr afia': 'Bibliografia',
    'prescrev er':  'prescrever',
    'solicit ar': 'solicitar',
    'analítica s ': 'analíticas ',
    'he matomas': 'hematomas',
    'exempl o': 'exemplo',
    'A informa ção apresentada': 'A informação apresentada',
    'endomé trio': 'endométrio',
    'consult a': 'consulta',
    'co nsultar': 'consultar',
    'C aso': 'Caso',
    ' tes te': ' teste',
    'computor izada': 'computorizada',
    'necessita m': 'necessitam',
    'tenha  alguma': 'tenha alguma',
    's ua': 'sua',
    'apres entada': 'apresentada',
    'algaliado s': 'algaliados',
    'ap licabilidade': 'aplicabilidade',
    'ten ha': 'tenha',
    'múlti plos': 'múltiplos',
    'u sar': 'usar',
    'adiar a': 'adiar',
    'e vitar': 'evitar',
    'computo rizada': 'computorizada',
    ' s ido ': ' sido ',
    'ressonância s magnética s': 'ressonâncias magnéticas',
    'diagnóst icos': 'diagnósticos',
    'est ando': 'estando',
    'po dem': 'podem',
    'c lopidogrel': 'clopidogrel',
    'd uas': 'duas',
    'cancr o': 'cancro',
    'individ ualizado': 'individualizado',


    'i nformação': 'informação',
    'in formação': 'informação',
    'inf ormação': 'informação',
    'info rmação': 'informação',
    'infor mação': 'informação',
    'inform ação': 'informação',
    'informa ção': 'informação',
    'informaç ão': 'informação',
    'informaçã o': 'informação',

    'a presentada': 'apresentada',
    'ap resentada': 'apresentada',
    'apr esentada': 'apresentada',
    'apre sentada': 'apresentada',
    'apres entada': 'apresentada',
    'aprese ntada': 'apresentada',
    'apresen tada': 'apresentada',
    'apresent ada': 'apresentada',
    'apresenta da': 'apresentada',
    'apresentad a': 'apresentada',

    'n esta': 'nesta',
    'ne sta': 'nesta',
    'nes ta': 'nesta',
    'nest a': 'nesta',

    'r ecomendação': 'recomendação',
    're comendação': 'recomendação',
    'rec omendação': 'recomendação',
    'reco mendação': 'recomendação',
    'recom endação': 'recomendação',
    'recome ndação': 'recomendação',
    'recomen dação': 'recomendação',
    'recomend ação': 'recomendação',
    'recomenda ção': 'recomendação',
    'recomendaç ão': 'recomendação',
    'recomendaçã o': 'recomendação',

    't em': 'tem',
    ' te m ': ' tem ',

    ' u m ': ' um ',

    'p ropósito': 'propósito',
    'pr opósito': 'propósito',
    'pro pósito': 'propósito',
    'prop ósito': 'propósito',
    'propó sito': 'propósito',
    'propós ito': 'propósito',
    'propósi to': 'propósito',
    'propósit o': 'propósito',

    'i nformativo': 'informativo',
    'in formativo': 'informativo',
    'inf ormativo': 'informativo',
    'info rmativo': 'informativo',
    'infor mativo': 'informativo',
    'inform ativo': 'informativo',
    'informa tivo': 'informativo',
    'informat ivo': 'informativo',
    'informati vo': 'informativo',
    'informativ o': 'informativo',

    'm édico': 'médico',
    'mé dico': 'médico',
    'méd ico': 'médico',
    'médi co': 'médico',
    'médic o': 'médico',

    'd úvida': 'dúvida',
    'dú vida': 'dúvida',
    'dúv ida': 'dúvida',
    'dúvi da': 'dúvida',
    'dúvid a': 'dúvida',

    's ubstitui': 'substitui',
    'su bstitui': 'substitui',
    'sub stitui': 'substitui',
    'subs titui': 'substitui',
    'subst itui': 'substitui',
    'substi tui': 'substitui',
    'substit ui': 'substitui',
    'substitu i': 'substitui',

    'C aso': 'Caso',
    'Ca so': 'Caso',
    'Cas o': 'Caso',

    'd eve ':  'deve ',
    'de ve ':  'deve ',
    'dev e ':  'deve ',

    ' u ma ': ' uma ',
    ' um a ': ' uma ',

    'c onsultar': 'consultar',
    'co nsultar': 'consultar',
    'con sultar': 'consultar',
    'cons ultar': 'consultar',
    'consu ltar': 'consultar',
    'consul tar': 'consultar',
    'consult ar ': 'consultar ',
    'consulta r ': 'consultar ',

    'a ssistente': 'assistente',
    'as sistente': 'assistente',
    'ass istente': 'assistente',
    'assi stente': 'assistente',
    'assis tente': 'assistente',
    'assist ente': 'assistente',
    'assiste nte': 'assistente',
    'assisten te': 'assistente',
    'assistent e': 'assistente',

    'd esta': 'desta',
    'de sta': 'desta',
    'des ta ': 'desta ',
    'dest a': 'desta',


    'c onteúdo': 'conteúdo',
    'co nteúdo': 'conteúdo',
    'con teúdo': 'conteúdo',
    'cont eúdo': 'conteúdo',
    'conte údo': 'conteúdo',
    'conteú do': 'conteúdo',
    'conteúd o': 'conteúdo',


    'a plicabilidade': 'aplicabilidade',
    'ap licabilidade': 'aplicabilidade',
    'apl icabilidade': 'aplicabilidade',
    'apli cabilidade': 'aplicabilidade',
    'aplic abilidade': 'aplicabilidade',
    'aplica bilidade': 'aplicabilidade',
    'aplicab ilidade': 'aplicabilidade',
    'aplicabi lidade': 'aplicabilidade',
    'aplicabil idade': 'aplicabilidade',
    'aplicabili dade': 'aplicabilidade',
    'aplicabilid ade': 'aplicabilidade',
    'aplicabilida de': 'aplicabilidade',
    'aplicabilidad e': 'aplicabilidade',

    'A informação apresentada nesta recomendação tem um propósito informativo e não substitui uma consulta com um médico. Caso tenha alguma dúvida sobre o conteúdo desta recomendação e a sua aplicabilidade no seu caso particular, deve consultar o seu médico assistente.': '',
    '.  ': '.',
    '.Justificação': '. Justificação',

}
# Define the replacements

# Replace the text content
text_processed = pdf_text
for old, new in replacements.items():
    text_processed = text_processed.replace(old, new)
#print(text_processed)


'''# Convert the text to lowercase and split it into words
words = text_processed.lower().split()

# Get the frequency of each word
word_counts = collections.Counter(words)

# Print the word counts
for word, count in word_counts.items():
    print(word, count)'''


# Find all the matches of the pattern
pattern = r'Recomendação (Escolha.*?)Bibliografia'
matches = re.findall(pattern, text_processed, flags=re.UNICODE)
#print(matches)

# Print each match
'''
for match in matches:
    print(match.strip())
    print('##########')
'''

# Save the text content to a csv file
with open('data/Recomendações_choosing_wisely_'+formatted_date+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Recomendação'])
    for i, string in enumerate(matches):
        writer.writerow([i, string])

# Save the text content to a text file
'''
with open('Recomendações_choosing_wisely_2'+formatted_date+'.txt', 'w') as f:
    f.write(text_processed)
'''