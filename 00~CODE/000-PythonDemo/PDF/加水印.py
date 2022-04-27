import PyPDF2

fileName = "/Users/weiyang/Desktop/NewTest.pdf"
fileName2 = "/Users/weiyang/Desktop/WaterMark.pdf"
fileName3 = "/Users/weiyang/Desktop/Result.pdf"
file = open( fileName, 'rb' )

reader = PyPDF2.PdfFileReader( file )
waterMarkReader = PyPDF2.PdfFileReader( open( fileName2, "rb" ) )
writer = PyPDF2.PdfFileWriter()

for pageIndex in range( reader.numPages ):
    pageObj = reader.getPage( pageIndex )
    pageObj.mergePage( waterMarkReader.getPage( 0 ) )
    writer.addPage( pageObj )

resultFile = open( fileName3, "wb" )
writer.write( resultFile )
resultFile.close()
file.close()