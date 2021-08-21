import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
# import sys
# new comment
# inputs = sys.argv[1:]

# #this function combines multiple pdfs into one
# def pdf_combiner(pdf_list):
#   merger = PyPDF2.PdfFileMerger()
#   for pdf in pdf_list:
#     print(pdf)
#     merger.append(pdf)
#   merger.write('super.pdf')

# pdf_combiner(inputs)

#this operation creates a new pdf
#and rotates the page 
# with open('dummy.pdf', 'rb') as file:
#   #  have to use rb to read binary
#   # print(file)
#   reader = PyPDF2.PdfFileReader(file)
#   # print(reader.numPages)
#   page = reader.getPage(0)
#   page.rotateCounterClockwise(90)
#   # in order to save the changes made to the pdf,
#   # we use the following
#   writer = PyPDF2.PdfFileWriter()
#   writer.addPage(page)
#   with open('tilt.pdf', 'wb') as new_file:
#     writer.write(new_file)