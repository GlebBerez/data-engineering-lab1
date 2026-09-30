import pandas as pd

df=pd.read_csv('morbidity.csv')
df.to_parquet("morbidity.parquet",index=False)