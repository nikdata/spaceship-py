# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['impute_missing_values']

# %%
import pandas as pd

df = pd.read_csv(upstream['impute_missing_values']['data'])

df[['group_number','pass_slot']] = df.passengerid.str.split("_", expand=True)

df[['deck','number','side']] = df.cabin.str.split('/', expand=True)

# write out file
df.to_csv(product['data'], index=False)