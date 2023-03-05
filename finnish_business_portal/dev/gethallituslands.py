from PyPDF2 import PdfReader
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")
import faker
import numpy as np
import pandas as pd
from selenium.webdriver.common.by import By
from urllib import request
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome, ChromeOptions
from finnish_business_portal.utils.myfiles import add_home
from pathlib import Path

incsv ='../../data/firmorfrom20150101.csv'
outcsv=incsv.replace('.csv','_lands.csv')
indf = pd.read_csv(incsv)
url = "https://virre.prh.fi/novus/companySearch?execution=e9s8#search-result"


options = ChromeOptions()
chrome_prefs = {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "download.open_pdf_in_system_reader": False,
    "profile.default_content_settings.popups": 0,
    "download.default_directory": "/home/hu-mka/Downloads",
}
options.add_experimental_option("prefs", chrome_prefs)
options.add_argument("−−incognito")
#options = {}
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
result={'id':[], 'lands':[]}
for index, row in indf.iterrows():
    browser.get(url)

    #driver.maximize_window()
    time.sleep(5) #
    print(f"search for business id :{row['businessId']}")
    result['id'].append(row['businessId'])
    tyhjenna = browser.find_element(By.CLASS_NAME, "btn-reset")
    tyhjenna.click()
    business = browser.find_element(By.ID, "businessId")
    business.send_keys(str(row['businessId']).strip())
    button = browser.find_element(By.NAME, "_eventId_search")
    button.click()

    try:
        table = browser.find_element(By.ID, "foundCompanies")
    except:
        result['lands'].append(None)
        continue
    print(table)
    rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    for row in rows:
        # Get the columns (all the column 2)
        col = row.find_elements(By.TAG_NAME, "td") #note: index start from 0, 1 is col 2
        if len(col)==0:
            continue
        break
    print(col[0].text) #prints text from the element
    col[0].click()
    try:
        button = browser.find_element(By.NAME, "_eventId_createElectronicTRExtract")
        button.click()
    except:
        result['lands'].append(None)
        continue
    browser.get("https://virre.prh.fi/novus/reportdisplay")
    time.sleep(1)

    reader = PdfReader(add_home('~/Downloads/reportdisplay.pdf'))

    # printing number of pages in pdf file
    print(len(reader.pages))

    # getting a specific page from the pdf file
    try:
        page = reader.pages[1]
    except:
        page = reader.pages[0]


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
            lands.append(data.split(',')[-2].split()[0])

    print(f"lands {lands}")
    Path(add_home('~/Downloads/reportdisplay.pdf')).unlink(missing_ok=True)

    #browser.get("https://virre.prh.fi/novus/reportdisplay.pdf")

    #response = request.urlopen("https://virre.prh.fi/novus/reportd")
    #file = open("FILENAME.pdf", 'wb')
    #file.write(response.read())
    #file.close()
    if len(lands) == 0:
        result['lands'].append(None)
    else:
        result['lands'].append((" ").join(lands))
    df = pd.DataFrame(result)
    df.to_csv(outcsv)

    time.sleep(2)
