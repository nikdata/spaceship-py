# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None


# %%
import pandas as pd


# %%
df = pd.read_csv('data/train.csv', sep=',')

# %%
new_cols = df.columns.str.lower()

df.columns = new_cols
# %%
# write out file
df.to_csv(product['data'], index=False)
