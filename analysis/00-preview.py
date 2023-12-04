
# import libraries ----
import polars as pl
import polars.selectors as cs
import altair as alt

alt.data_transformers.enable("vegafusion")

# import datafiles ----

tbl_rawtrain = pl.read_csv('../data/train.csv')
tbl_rawtest = pl.read_csv('../data/test.csv')


# preview the data ----

tbl_rawtrain.head()
tbl_rawtest.head() # missing column transported

# size
tbl_rawtrain.shape
tbl_rawtest.shape

# we should make the columns all lowercase ----
better_columns = [i.lower() for i in tbl_rawtrain.columns]

tbl_rawtrain.columns = better_columns
# the test file does not have the column transported
tbl_rawtest.columns = better_columns[0:13]

### Missing values ----

tbl_rawtrain \
    .null_count() \
    .melt(value_name='missing') \
    .with_columns(pl.Series(name = 'type', values = tbl_rawtrain.dtypes)) \
    .with_columns((pl.col('missing') / tbl_rawtrain.shape[0]).alias('pct_missing'))


### COLUMN EXPLORATION ###

tbl_rawtrain \
    .select(pl.col('passengerid')) \
    .n_unique()

tbl_rawtrain.select(pl.col('passengerid')).head()

# passengerid has group & passenger within group
# let's find out how many groups there are

tbl_passgroup = tbl_rawtrain.select(pl.col('passengerid').str.split_exact("_",1)).unnest("passengerid").rename({'field_0':'group', 'field_1':'passenger'})

tbl_passgroup.group_by(pl.col('group')).count().sort(by = pl.col('count'), descending=True)

# split the cabin column too

cln_train1 = tbl_rawtrain \
    .with_columns(pl.col('passengerid') \
                  .str.split_exact('_',1) \
                  .struct.rename_fields(['group','passenger']) \
                  .alias('fields')) \
    .unnest("fields") \
    .with_columns(pl.col('cabin') \
                  .str.split_exact('/',2) \
                  .struct.rename_fields(['deck','cabin_number','side']) \
                  .alias('fields')) \
    .unnest('fields')

# histogram of the age using altair

alt.Chart( \
    cln_train1, \
    title = alt.Title('Distribution of Age') \
    ) \
    .mark_bar() \
    .encode( \
        alt.X('age', bin = True).title('Age'), \
        alt.Y('count()').title('Count') \
    )    

