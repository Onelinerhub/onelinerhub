# How to create dataframe from JSON

```python
import pandas as pd
json = '''{"Phone":["ip5","ip6","ip8","sms","xi"],"Price":[204,304,404,405,305],"Color":["red","red","gray","black","red"]}'''
df = pd.read_json(json)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `.read_json(` - will parse specified JSON string and create dataframe

group: json

## Example: 
```python
import pandas as pd
jsonStr = '''{"Phone":["ip5","ip6","ip8","sms","xi"],"Price":[204,304,404,405,305],"Color":["red","red","gray","black","red"]}'''
df = pd.read_json(jsonStr)
print(df)
```
```
  Phone  Price  Color
0   ip5    204    red
1   ip6    304    red
2   ip8    404   gray
3   sms    405  black
4    xi    305    red

```

