""" get all companies of year 2017 the days with problems"""

import finnish_business_portal as busportal
from datetime import datetime, timedelta
import pandas as pd

portal = busportal.SearchModel("BisCompany", loop_results=True, deep=False)

mydates = [
    datetime(year=2017, month=3, day=16),
    datetime(year=2017, month=3, day=16),
    datetime(year=2017, month=5, day=4),
    datetime(year=2017, month=5, day=18),
    datetime(year=2017, month=5, day=23),
    datetime(year=2017, month=9, day=28),
]
dfs = []
for mydate in mydates:
    print(mydate)
    portal.search(
        companyRegistrationFrom=mydate.strftime("%Y-%m-%d"),
        companyRegistrationTo=(mydate + timedelta(days=1)).strftime("%Y-%m-%d"),
        maxResults=100,
    )
    dfs.append(portal.to_frame().results)

    df = pd.concat(dfs)
    df.to_csv("fix_firmor2017.csv")
