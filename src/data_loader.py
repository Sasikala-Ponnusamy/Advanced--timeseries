import pandas as pd
def load_data("/content/store_sales.csv")
df=pd.read_csv("/content/store_sales.csv")
df['date']=pd.to_datetime(df['date'])
df.sort_values('date',inplace=True)
return df
