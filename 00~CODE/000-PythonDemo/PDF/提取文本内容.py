import PyPDF2
import os

fileName = "F:/eBook/test/algebra.pdf"
file = open( fileName, 'rb' )
reader = PyPDF2.PdfFileReader( file )
page = reader.getPage(4)
content = page.extractText()
print(content)
file.close()