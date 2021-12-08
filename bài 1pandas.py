import pandas as pd
data = {"a":pd.Series([3,48,66,58774],index=[1,2,3,4]),"b": pd.Series([5848,9887,4543,43345],index=[1,2,3,4])}
df = pd.DataFrame(data)
print('in cột đầu của series:')
print(df["a"])