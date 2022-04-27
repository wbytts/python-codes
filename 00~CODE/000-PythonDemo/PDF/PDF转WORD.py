def removeWatermark(wm_text, inputFile, outputFile):
    from PyPDF4 import PdfFileReader, PdfFileWriter
    from PyPDF4.pdf import ContentStream
    from PyPDF4.generic import TextStringObject, NameObject
    from PyPDF4.utils import b_

    with open(inputFile, "rb") as f:
        source = PdfFileReader(f, "rb")
        output = PdfFileWriter()

        for page in range(source.getNumPages()):
            page = source.getPage(page)
            content_object = page["/Contents"].getObject()
            content = ContentStream(content_object, source)

            # for operands, operator in content.operations:
            #     if operator == b_("Tj"):
            #         text = operands[0]
            #         print(text, end='')

            #         if isinstance(text, str) and text.startswith(wm_text):
            #             operands[0] = TextStringObject('')

            print(content_object)
            page.__setitem__(NameObject('/Contents'), content)
            output.addPage(page)

        with open(outputFile, "wb") as outputStream:
            output.write(outputStream)

wm_text = '福昕PDF编辑器'
inputFile = r'F:/eBook/test/lmx2572_wrapper.pdf'
outputFile = r"F:/eBook/test/res.pdf"
removeWatermark(wm_text, inputFile, outputFile)