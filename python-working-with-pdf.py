import PyPDF2
# note the capitalization
import os

# execute inside python-learning directory (directory inside which this py file is present)
os.chdir("./Complete-Python-3-Bootcamp-master/15-PDFs-and-Spreadsheets")

# Notice we read it as a binary with 'rb'
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f)
print("\n\nlen(pdf_reader.pages) => ", len(pdf_reader.pages))

print("\n\n============================================\n\n")

page_one = pdf_reader.pages[0]
page_one_text = page_one.extract_text()
print("page_one_text => \n", page_one_text)

print("\n\n============================================\n\n")

f.close()

# adding page to PDFs
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f)
page_number = 0
page_one = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter()
pdf_writer.add_page(page_one)
pdf_output = open("Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)
f.close()

# printing all text content of a PDF
f = open('Working_Business_Proposal.pdf','rb')
# List of every page's text.
# The index will correspond to the page number.

pdf_reader = PyPDF2.PdfReader(f)

for p in range(len(pdf_reader.pages)):
    
    page = pdf_reader.pages[p]
    print(page.extract_text())
    print("\n\n============================================\n\n")
