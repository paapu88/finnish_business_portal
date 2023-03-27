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
from bs4 import BeautifulSoup

incsv ='../../data/firmor2015.csv'
outcsv=incsv.replace('.csv','_lands.csv')
df = pd.read_csv(incsv)
url = "https://virre.prh.fi/novus/home?execution=e5s1"


options = ChromeOptions()
chrome_prefs = {
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "download.open_pdf_in_system_reader": False,
    "profile.default_content_settings.popups": 0,
    "download.default_directory": "/home/hu-mka/Downloads",
}
options.add_experimental_option("prefs", chrome_prefs)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

problem_ones = ["2673443-2","2674564-1","2674060-5","2675811-9","2676306-5","2677768-6","2680347-7"]
for index, row in df.iterrows():
    if str(row['businessId']).strip() in problem_ones:
        print(f"skipping problem {row['businessId']}")
        continue
    current_company_file = f"./firmor/{str(row['businessId']).strip()}_tiedot.csv"
    print(current_company_file)
    if Path(current_company_file).exists():
        print(f"{current_company_file} exists, continuing...")
        continue
    ok=False
    while not ok:
        try:
            browser.get(url)
            #browser.refresh()
            #driver.maximize_window()
            time.sleep(1.6) #
            print(f"search for business id :{row['businessId']}")
            #result['id'].append(row['businessId'])
            business = browser.find_element(By.ID, "criteriaText")
            business.clear()
            business.send_keys(str(row['businessId']).strip())
            time.sleep(0.8)
            hae = browser.find_element(By.NAME, "_eventId_search")
            hae.click()
            #table = browser.find_element(By.ID, "foundCompanies")
            time.sleep(1.6)
            html = browser.page_source

            df = pd.read_html(html)
            df[0].to_csv(current_company_file)
            ok=True
        except:
            print("sleeping due to problems...")
            time.sleep(15)

            ok=False
    #print(df)
    #print(f"{str(row['businessId']).strip()}_tiedot.csv")
    time.sleep(4.0)