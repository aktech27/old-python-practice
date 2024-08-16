from PyPDF2 import PdfFileReader as pdr
import tabula as tl
pdfloc=r"D:/BCA AK/Sem 4/JAVA book.pdf"
pdfloc1=r"D:/VICTORY INDUSTRIES/2019-2020/Bills/INVOICE001.pdf"
pdfFO=open(pdfloc,"rb")
pdfRead=pdr(pdfFO)
print(pdfRead.numPages)
print(pdfRead.getPage(0).extractText())
pdfFO.close()

df=tl.read_pdf(pdfloc1,pages="all")
print(df)
