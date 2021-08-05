import PyPDF2

with open('dummy.pdf', 'rb') as file:
  #  have to use rb to read binary
  # print(file)
  reader = PyPDF2.PdfFileReader(file)
  # print(reader.numPages)
  page = reader.getPage(0)
  page.rotateCounterClockwise(90)
  # in order to save the changes made to the pdf,
  # we use the following
  writer = PyPDF2.PdfFileWriter()
  writer.addPage(page)
  with open('tilt.pdf', 'wb') as new_file:
    writer.write(new_file)