import pandas as pd
import re
from mechanize import Browser

df = pd.read_csv('../../data/firmor2015.csv')
br = Browser()
br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Firefox')]

#br.open("https://virre.prh.fi/novus/finStateSearch?execution=e6s1")
br.open("https://virre.prh.fi/novus/home?execution=e5s1")
for index, row in df.iterrows():
    print(br.forms())
    print(row['businessId'])
    br.select_form(ls_form='businessId')
    response = br.submit()
    print(f"response: {response}")
    sys.exit()



# Ignore robots.txt
# Google demands a user-agent that isn't a robot

