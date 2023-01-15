from PyPDF2 import PdfMerger, PdfFileReader
import os

merger=PdfMerger()

for items in os.listdir():
	if items.endswith('.pdf'):
		merger.append(items)
	

merger.write("merged_pdf.pdf")
merger.close()