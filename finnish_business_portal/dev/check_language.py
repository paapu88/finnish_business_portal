import pandas as pd
df = pd.read_csv('../../data/firmorfrom20150101.csv')

endf = df[ [col for col in df.columns if col[0].startswith("contactDetails")]].stack(0).query('language == "EN" & endDate != endDate').dropna(how="all", axis=1)


print(endf)