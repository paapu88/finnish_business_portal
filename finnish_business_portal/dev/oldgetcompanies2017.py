""" get all companies of year 2017 """

import finnish_business_portal as busportal
from datetime import datetime, timedelta
import pandas as pd

portal = busportal.SearchModel("BisCompany",loop_results=True, deep=False)

mydate = datetime(year=2017, month=1, day=1)

maxdate = datetime(year=2018, month=1, day=1)
dfs=[]
while mydate < maxdate:
    print(mydate)
    portal.search(companyRegistrationFrom=mydate.strftime('%Y-%m-%d'),
                  companyRegistrationTo=(mydate+timedelta(days=1)).strftime('%Y-%m-%d'), maxResults=50)
    dfnow = portal.to_frame().results
    if dfnow is not None and len(dfnow)> 0:
        dfs.append(dfnow)
    else:
        print(f"WARNING: no data for date {mydate}")
    mydate = mydate +timedelta(days=1)

    df = pd.concat(dfs)
    df.to_csv('firmor2017.csv')

# errors
"""
2017-03-16
2017-05-04
2017-05-18
2017-05-23 00:00:00
2017-09-28 00:00:00
"""