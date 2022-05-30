from PyPDF2 import PdfFileMerger, PdfFileReader

# Lista de PDFs que serão mergeados
lista_pdfs = ['arquivo1.pdf', 'arquivo2.pdf', 'arquivo3.pdf']

mergedObject = PdfFileMerger()

# Loop para inserir os arquivos na lista de merge
for file_name in lista_pdfs:
    mergedObject.append(PdfFileReader(file_name, 'rb'))

# Junta os arquivos selecionados
mergedObject.write("Documento.pdf")

