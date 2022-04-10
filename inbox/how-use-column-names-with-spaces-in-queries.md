# How to use column name with spaces in queries

```python
import pandas as pd

#Apartments
apartments = pd.DataFrame(columns=['Area m2', 'Age', '#Rooms'])

apartments['Area m2'] = [105, 224, 49, 20]
apartments['Age'] = [3, 5, 1, 1]
apartments['#Rooms'] = [2, 4, 1, 1]

print("All apartments")
print(apartments)

small_apartments = apartments.query('`Area m2` < 25')
print("Small")
print(small_apartments)

lucky = apartments[apartments.Age == apartments['#Rooms']]
print("Lucky")
print(lucky)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates DataFrame named 'apartments' with given column names[DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- line 9 through line 11 - assign apartment characteristics
- ``apartmens.query('`Area m2` < 25')`` - Return the apartments with area less than 25 square meters. You can refer to column names that are not valid Python variable names by surrounding them in backticks. This includes column names with spaces in them [DataFrame.query](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html)
- `apartments[apartments.Age == apartments['#Rooms']]` - Return apartmens where age is equal to number of rooms. You can also use boolean indexing to access invalid column names. In this case, the column name contains `#` character, which is used for python comments

## Output: 
```
All apartments
   Area m2  Age  #Rooms
0      105    3       2
1      224    5       4
2       49    1       1
3       20    1       1
Small
   Area m2  Age  #Rooms
3       20    1       1
Lucky
   Area m2  Age  #Rooms
2       49    1       1
3       20    1       1
```
