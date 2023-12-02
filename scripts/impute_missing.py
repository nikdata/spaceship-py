# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['initial_cleaning']

# %%
import pandas as pd

# %%
# read in the source file
df = pd.read_csv(upstream['initial_cleaning']['data'])

# %%

# impute values with median
df['age'] = df.age.fillna(df.age.median)
df['rommservice'] = df.roomservice.fillna(df.roomservice.median)
df['foodcourt'] = df.foodcourt.fillna(df.foodcourt.median)
df['shoppingmall'] = df.shoppingmall.fillna(df.shoppingmall.median)
df['spa'] = df.spa.fillna(df.spa.median)
df['vrdeck'] = df.vrdeck.fillna(df.vrdeck.median)

# impute the boolean
df['missing_cryo'] = 0
df.loc[df['cryosleep'].isna() == True, 'missing_cryo'] = 1
df['cryosleep'] = df['cryosleep'].fillna(False)

df['missing_vip'] = 0
df.loc[df['vip'].isna() == True, 'missing_vip'] = 1
df['vip'] = df['vip'].fillna(False)

# impute missing char columns
df['missing_home'] = 0
df.loc[df['homeplanet'].isna() == True, 'missing_home'] = 1
df['homeplanet'] = df['homeplanet'].fillna('unknown')

df['missing_cabin'] = 0
df.loc[df['cabin'].isna() == True, 'missing_cabin'] = 1
df['cabin'] = df['cabin'].fillna('unknown')

df['missing_destination'] = 0
df.loc[df['destination'].isna() == True, 'missing_destination'] = 1
df['destination'] = df['destination'].fillna('unknown')

df['missing_name'] = 0
df.loc[df['name'].isna() == True, 'missing_name'] = 1
df['name'] = df['name'].fillna('unknown')

# %%
# write out file

df.to_csv(product['data'], index = False)
