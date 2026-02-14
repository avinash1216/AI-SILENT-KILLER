import sqlite3
import pandas as pd

# connect
conn = sqlite3.connect("../data/database.db")

# load raw data
raw_df = pd.read_csv("../data/raw/raw_events.csv")

# write raw into db
raw_df.to_sql("raw_events", conn, if_exists="replace", index=False)

# now use SQL for transformations
