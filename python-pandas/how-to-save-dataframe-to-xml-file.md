# How to save dataframe to XML file

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df.to_xml('/path/to/file.xml');
```


group: xml


