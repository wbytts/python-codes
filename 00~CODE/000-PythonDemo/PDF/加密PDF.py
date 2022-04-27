import PyPDF2

fileName = "F:/eBook/test/algebra.pdf"
newFileName = "F:/eBook/test/algebra_res.pdf"

file = open(fileName, 'rb')
reader = PyPDF2.PdfFileReader(file)
writer = PyPDF2.PdfFileWriter()

for pageIndex in range(reader.numPages):
    writer.addPage(reader.getPage(pageIndex))

writer.encrypt('bell')  # passwd
newFile = open(newFileName, "wb")
writer.write(newFile)

newFile.close()
file.close()
