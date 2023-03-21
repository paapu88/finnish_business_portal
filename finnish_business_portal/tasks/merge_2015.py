import pandas as pd
df1 = pd.read_csv('../../data/firmorfrom20150101.csv', index_col=0)
df2 = pd.read_csv('../../data/firmorfrom20151110.csv', index_col=0)
df = pd.concat([df1,df2])

df = df.drop_duplicates()
df = df.loc[df['companyForm'].isin(['OY','OYJ'])]
#mask = df['name'].str.len()==0
#df.drop(mask)
df = df[df['name'].notna()]
df.to_csv('../../data/firmor2015.csv')
df['lig'] = df.apply(lambda x: len(x.liquidations), axis=1)
dfliq = df[(df.lig > 2)]
dfliq.to_csv('../../liqs.csv')



