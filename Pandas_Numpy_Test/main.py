import pandas as pd

what = pd.read_table('http://bit.ly/movieusers', sep='|').head()

print(what)