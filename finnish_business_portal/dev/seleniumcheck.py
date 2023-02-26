
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
1
2
3
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
browser.get(url)
for index, row in df.iterrows():
    #driver.maximize_window()
    time.sleep(5) #
    print(row['businessId'])

    business = browser.find_element(By.ID, "businessId")
    business.send_keys(row['businessId'])
    button = browser.find_element(By.ID, "_eventId_search")
    button.click()
    """
    <button type="submit" class="btn btn-primary " name="_eventId_search" id="_eventId_search" tabindex="" onclick="" style="">
			Search</button>
    """
    time.sleep(15) #

    sys.exit()