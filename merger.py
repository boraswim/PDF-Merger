from pypdf import PdfWriter
import os

merger = PdfWriter()

pdfs = os.listdir("./pdf")
pdfCount = 0

for pdf in pdfs:
    if(pdf.lower().endswith(".pdf")):
        pdfCount+=1
        merger.append("./pdf/" + pdf)

if(pdfCount > 0):
    merger.write("merged-pdf.pdf")
    print("PDF merge completed. (merged-pdf.pdf)")
else:
    print("No PDF file was found.")

merger.close()
