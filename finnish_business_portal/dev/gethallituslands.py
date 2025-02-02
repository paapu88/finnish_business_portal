import random

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
from fp.fp import FreeProxy


# Get free proxies for rotating
def get_free_proxies(driver):
    driver.get('https://sslproxies.org')

    table = driver.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)

    return proxies

proxies = [{"http": 'http://78.47.16.54:80', "https": 'http://78.47.16.54:80'},
    {"http": 'http://203.75.190.21:80', "https": 'http://203.75.190.21:80'}]

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
#options.add_argument("--headless")

#options.add_argument("−−incognito")
#options = {}
#browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#free_proxies = get_free_proxies(browser)


result={'id':[], 'lands':[]}
iproxy=None
for index, row in indf.iterrows():
    ok = False
    while not ok:
        #proxy = FreeProxy(rand=True, timeout=1, country_id=['FI','SE']).get()
        if iproxy is None or iproxy==20:
            iproxy=0
            proxy_ok=False
            while not proxy_ok:
                try:
                    proxy = FreeProxy(rand=True, elite=True, https=True).get()
                    proxy_ok=True
                except:
                    print(f"sleeping and waiting for proxy...")
                    time.sleep(20)
        iproxy+=1
        print(f"proxy: {proxy}")
        try:
            options.add_argument('--proxy-server=' + proxy)
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

            browser.get(url)

            #driver.maximize_window()
            time.sleep(2) #
            print(f"search for business id :{row['businessId']}")
            result['id'].append(row['businessId'])
            tyhjenna = browser.find_element(By.CLASS_NAME, "btn-reset")
            tyhjenna.click()
            time.sleep(2) #

            business = browser.find_element(By.ID, "businessId")
            business.send_keys(str(row['businessId']).strip())
            button = browser.find_element(By.NAME, "_eventId_search")
            button.click()
            time.sleep(2) #

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
            time.sleep(2) #

            try:
                button = browser.find_element(By.NAME, "_eventId_createElectronicTRExtract")
                button.click()
            except:
                result['lands'].append(None)
                continue
            browser.get("https://virre.prh.fi/novus/reportdisplay")
            time.sleep(2)

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
            print(f"sleeping after good result!")
            time.sleep(20)
            ok=True
        except:
            ok=False