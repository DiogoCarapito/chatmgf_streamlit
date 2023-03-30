from pdfminer.high_level import extract_pages, extract_text

'''for page_layout in extract_pages('data/Programa-Nacional-Vigilancia-Gravidez-Baixo-Risco-2015.pdf'):
    for element in page_layout:
        print(element)'''

text = extract_text('../data/Programa-Nacional-Vigilancia-Gravidez-Baixo-Risco-2015.pdf')

text = text.replace('\n\n', '\n')
text = text.replace('-\n', '')


with open('../data/PNGBR.txt', 'w') as file:
    file.write(text)

#with open('data/PNGBR_sem_paragrafos.txt', 'w') as file:
#    file.write(text_sem_paragrafos)
