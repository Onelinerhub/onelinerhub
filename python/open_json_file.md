# How to open JSON file

```python
import json
with open('/tmp/data.json') as f:
  obj = json.load(f)
```

- /tmp/data.json - path to JSON file
- json.load - parse json object in file and gives result in dictionary

group: json


## Example
```python
import json
with open('/tmp/data.json') as f:
  obj = json.load(f)
  print(obj)
```
```bash
{'test': 1}
```

group: json
