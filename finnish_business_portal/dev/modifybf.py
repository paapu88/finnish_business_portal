# take only years 2015-2019

import pandas as pd
import re

def cleanup(txt):
    return re.sub("[^0-9^.^,]", "", txt)


df = pd.read_csv("../../data/businessFinlandMaksetutTuetLAinen20102022.csv")
print(df.describe())
print(df.head())
print(df.columns)
df = df[df['Maksuvuosi'].isin([2015,2016,2017,2018,2019])]
print(df.head())
for col in ['Avustus €', 'Laina €','EAKR-rahoitus €', 'Tutkimusrahoitus €', 'Yhteensä €']:
    df[col] = df[col].apply(cleanup)
    df[col]=pd.to_numeric(df[col])
print(df.head())
print(df.describe())
df.to_csv("../../data/businessFinlandMaksetutTuetLAinen20152019.csv")
