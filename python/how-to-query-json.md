# How to query json

```python
import json
json = '{"ids":{"id": 1}}'
data = json.loads(json)
id = data['ids']['id']
```


group: json

## Example: 
```python
import json
json = '{"ids":{"id":"1"}}'
data = json.loads(json)
id = data['ids']['id']
print(id)
```
