# How to use one hot encoder

```python
import pandas as pd

ages = [50, 51, 52, 45, 40, 56]
countries = ['USA', 'Ukraine', 'Ukraine', 'UK', 'UK']

df = pd.DataFrame(list(zip(ages, countries)), columns=['Age', 'Country'])

df = pd.get_dummies(df['Country'], prefix='Country')
print(df.head())
```


group: encoder

## Example: 
```python
import pandas as pd

ages = [50, 51, 52, 45, 40, 56]
countries = ['USA', 'Ukraine', 'Ukraine', 'UK', 'UK']

df = pd.DataFrame(list(zip(ages, countries)), columns=['Age', 'Country'])
print(df)

oh = pd.get_dummies(df['Country'], prefix='Country')
df = df.join(oh)
df.drop('Country', axis=1, inplace=True)
print(df)
```
```
   Age  Country
0   50      USA
1   51  Ukraine
2   52  Ukraine
3   45       UK
4   40       UK
   Age  Country_UK  Country_USA  Country_Ukraine
0   50           0            1                0
1   51           0            0                1
2   52           0            0                1
3   45           1            0                0
4   40           1            0                0

```

