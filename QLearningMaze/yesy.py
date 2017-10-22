import datetime
import pandas as pd
import numpy as np

for i in range (3*2):
    print(i)

table = np.array([20, 20])

print(table)

todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')

columns = ['A','B', 'C']

df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0) # with 0s rather than NaNs

print(df_)

df_ = df_.append(
    pd.Series(
        [0]*2,
        index=[0, 1],
        name='0',
    )
)

print(df_)


S = [0, 20]

print(str(S))
print(df_.ix[10, :].index)
print(df_.reindex(np.random.permutation(df_.ix[10, :].index)))
