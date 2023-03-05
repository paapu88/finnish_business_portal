from PyPDF2 import PdfReader
from finnish_business_portal.utils.myfiles import add_home

# creating a pdf reader object
reader = PdfReader(add_home('~/Downloads/reportdisplay.pdf'))

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page = reader.pages[1]

# extracting text from page
text = page.extract_text()
print(type(text))
print(len(text))
print(text.splitlines())
found = False
lands = []
for data in text.splitlines():
    if data=="VOIMASSAOLEVAT HENKILÖTIEDOT":
        found = True
        continue
    if found and data.isupper():
        break
    if found:
        lands.append(data.split(',')[-1].strip())
print(f"lands {lands}")
