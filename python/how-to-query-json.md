# How to query json

```python
import json
data = json.loads('{"ids":{"id":"5"}}')
id = data['ids']['id']
```

- `import json` - library to operate with json
- `json.loads` - parse json string into object
- `data['ids']['id']` - query value of the nested element the same was as we query dictionary

group: json

## Example: 
```python
import json
data = json.loads('{"ids":{"id":"5"}}')
id = data['ids']['id']
print(id)
```
```
5

```
