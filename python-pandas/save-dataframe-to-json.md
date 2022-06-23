# Save dataframe to JSON

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

json = df.to_json()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `to_json()` - saves dataframe to JSON string

group: json

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305],
  'Color': ['red', 'red', 'gray', 'black', 'red']
})

json = df.to_json()
print(json)
```
```
{"Phone":{"0":"ip5","1":"ip6","2":"ip8","3":"sms","4":"xi"},"Price":{"0":204,"1":304,"2":404,"3":405,"4":305},"Color":{"0":"red","1":"red","2":"gray","3":"black","4":"red"}}

```

