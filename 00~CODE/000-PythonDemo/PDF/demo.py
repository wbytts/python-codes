from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4.pdf import ContentStream
from PyPDF4.generic import TextStringObject, NameObject
from PyPDF4.utils import b_

inputFile = r'F:/eBook/test/lmx2572_wrapper.pdf'

with open(inputFile, "rb") as f:
    source = PdfFileReader(f, "rb")
    output = PdfFileWriter()
    
    page = source.getPage(3)
    objects = page.getObject()
    print(3, objects)

    objects_4 = source.getPage(4).getObject()
    print(4, objects_4)

    # for i in range(source.getNumPages()):
    #     page = source.getPage(i)
    #     # XObjects = page["/Xobject"].getObject()
        
    #     objects = page.getObject()

    #     #print(i, objects)
    #     print(i, objects['/Resources']['/XObject']['/Xf3'])

