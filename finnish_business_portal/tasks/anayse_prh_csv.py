import pandas as pd
from finnish_business_portal.utils.myfiles import add_home

df = pd.read_csv("~/git/Omat/HankenKandi/finnish_business_portal/data/firmor201401to04.csv")
print(df.info)
print(df.describe)

#df = df[df['liquidations'].astype(bool)]
#print(df.head())
df['lig'] = df.apply(lambda x: len(x.liquidations), axis=1)
dfliq = df[(df.lig > 2)]
dfliq.to_csv('liqs.csv')


