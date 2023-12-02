# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['initial_cleaning']

# %%
import pandas as pd

df = pd.read_csv(upstream['initial_cleaning']['data'])

#%% 
# let's find the missing values
tbl_missing = pd.DataFrame(df.isna().sum(), columns = ['missing']).reset_index()

# %%
# let's find the data types for each columm
tbl_types = pd.DataFrame(df.dtypes, columns = ['type']).reset_index()

#%%
# let's get the descriptive stats
tbl_stats = df.describe(include='all', percentiles=[0.10, 0.25, 0.50, 0.75, 0.80, 0.90, 0.95, 0.99]).transpose().reset_index()

#%%

# combine the datasets together
df_stats = tbl_missing.merge(tbl_types, left_on = ['index'], right_on = ['index'], how = 'inner').merge(tbl_stats, left_on=['index'], right_on=['index'], how='inner')

#%%

# write out the file
df_stats.to_csv(product['data'], index=False)