# How to save dataframe to XML file

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305]
})

df.to_xml('/path/to/file.xml');
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `to_xml` - saves dataframe to XML file
- `/path/to/file.xml` - path to write file to

group: xml

## Example: 
```python
cat /path/to/file.xml
```
```
<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <index>0</index>
    <Phone>ip5</Phone>
    <Price>204</Price>
  </row>
  <row>
    <index>1</index>
    <Phone>ip6</Phone>
    <Price>304</Price>
  </row>
  <row>
    <index>2</index>
    <Phone>ip8</Phone>
    <Price>404</Price>
  </row>
  <row>
    <index>3</index>
    <Phone>sms</Phone>
    <Price>405</Price>
  </row>
  <row>
    <index>4</index>
    <Phone>xi</Phone>
    <Price>305</Price>
  </row>
</data>
```

