import PyPDF2

fileName1 = "/Users/weiyang/Desktop/Test1.pdf"
fileName2 = "/Users/weiyang/Desktop/Test2.pdf"
newFileName = "/Users/weiyang/Desktop/NewTest.pdf"

file1 = open( fileName1, 'rb' )
file2 = open( fileName2, 'rb' )

reader1 = PyPDF2.PdfFileReader( file1 )
reader2 = PyPDF2.PdfFileReader( file2 )

writer = PyPDF2.PdfFileWriter()

for pageIndex in range( reader1.numPages ):
    writer.addPage( reader1.getPage( pageIndex ) )

for pageIndex in range( reader2.numPages ):
    writer.addPage( reader2.getPage( pageIndex ) )

newFile = open( newFileName, "wb" )
writer.write( newFile )
newFile.close()
file1.close()
file2.close()