"""
python getcompanies.py --year 2015 --month 11 --day 10
"""

import finnish_business_portal as busportal
from datetime import datetime, timedelta
import pandas as pd
import time
import argparse

parser = argparse.ArgumentParser(description="Download metno data ")
parser.add_argument(
    "--year",
    help="start year", type=int,
)
parser.add_argument(
    "--month",
    help="start month",type=int,
)
parser.add_argument(
    "--day",
    help="start month",type=int,
)
args = parser.parse_args()
busportal = busportal.SearchModel("BisCompany",loop_results=True, deep=True)

mydate = datetime(year=args.year, month=args.month, day=args.day)
init = mydate
maxdate = datetime(year=2019, month=12, day=31)
dfs=[]
while mydate < maxdate:
    print(mydate)
    portal = busportal.search(companyRegistrationFrom=mydate.strftime('%Y-%m-%d'),
                              companyRegistrationTo=(mydate+timedelta(days=1)).strftime('%Y-%m-%d'),
                              maxResults=2)
    try:
        dfnow = portal.to_frame().results
    except:
        dfnow = None
        time.sleep(10)
    if dfnow is not None and len(dfnow)> 0:
        dfs.append(dfnow)
    else:
        print(f"WARNING: no data for date {mydate}")
    mydate = mydate +timedelta(days=1)
    if len(dfs)>0:
        df = pd.concat(dfs)
        df.to_csv(f'../../data/firmorfrom{args.year}{str(args.month).zfill(2)}{str(args.day).zfill(2)}.csv')

# errors
"""
2017-03-16
2017-05-04
2017-05-18
2017-05-23 00:00:00
2017-09-28 00:00:00
"""