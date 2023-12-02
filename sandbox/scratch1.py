import pandas as pd

df = pd.read_csv('../data/train.csv')

df.head()

new_cols = df.columns.str.lower()

df.columns = new_cols

df[['group_number','pass_slot']] = df.passengerid.str.split("_", expand=True)

df[['deck','number','side']] = df.cabin.str.split('/', expand=True)

df

# let's find the missing values
tbl_missing = pd.DataFrame(df.isna().sum(), columns = ['missing']).reset_index()
tbl_types = pd.DataFrame(df.dtypes, columns = ['type']).reset_index()

tbl_stats = df.describe(include='all', percentiles=[0.10, 0.25, 0.50, 0.75, 0.80, 0.90, 0.95, 0.99]).transpose().reset_index()


tbl_missing.merge(tbl_types, left_on = ['index'], right_on = ['index'], how = 'inner').merge(tbl_stats, left_on=['index'], right_on=['index'], how='inner')

