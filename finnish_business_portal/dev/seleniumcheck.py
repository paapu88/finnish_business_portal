
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

df = pd.read_csv('../../data/firmorfrom20150101.csv')
url = "https://virre.prh.fi/novus/finStateSearch?execution=e6s1"
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
for index, row in df.iterrows():
    browser.get(url)

    #driver.maximize_window()
    #time.sleep(5) #
    print(f"search for business id :{row['businessId']}")
    tyhjenna = browser.find_element(By.CLASS_NAME, "btn-reset")
    tyhjenna.click()
    business = browser.find_element(By.ID, "businessId")
    business.send_keys(str(row['businessId']).strip())
    button = browser.find_element(By.ID, "_eventId_search")
    button.click()
    #tilit = browser.find_element(By.ID, "finStatements")
    html = browser.page_source
    dfs = pd.read_html(html)
    #print(tilit)
    print(dfs[1]['Diaarinumero'])
    print(len(dfs[1]['Diaarinumero']))
    """
    <button type="submit" class="btn btn-primary " name="_eventId_search" id="_eventId_search" tabindex="" onclick="" style="">
			Search</button>
    """
    time.sleep(5) #

    #sys.exit()