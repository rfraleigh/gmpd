import os
import pandas as pd

data = pd.read_csv('gmpd.csv')
old_columns = data.columns
clean_columns = {item:item.lower().replace(' ','_').replace('&','') for item in old_columns}
data.rename(columns=clean_columns,inplace=True)

data.to_csv('gmpd_cleaned.csv',index=None)