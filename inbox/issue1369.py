import pandas as pd
series = pd.Series([1, 2, 3, 4, 5] ) #creating a series
lst = pd.Series.tolist(series) #turning the series back to a list
print(lst)