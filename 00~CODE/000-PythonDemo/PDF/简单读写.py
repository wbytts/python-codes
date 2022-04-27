from PyPDF2 import PdfFileReader, PdfFileWriter
infn = 'F:/eBook/test/lmx2572_wrapper.pdf'
outfn = 'F:/eBook/test/res.pdf'
# 获取一个 PdfFileReader 对象
pdf_input = PdfFileReader(open(infn, 'rb'))
# 获取 PDF 的页数
page_count = pdf_input.getNumPages()
print('页数', page_count)
# 获取一个 PdfFileWriter 对象
pdf_output = PdfFileWriter()
for i in range(page_count):
    # 返回一个 PageObject
    page = pdf_input.getPage(i)
    # 将一个 PageObject 加入到 PdfFileWriter 中
    pdf_output.addPage(page)

# 输出到文件中
pdf_output.write(open(outfn, 'wb'))