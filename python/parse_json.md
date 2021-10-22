# How to parse JSON

```python
import json
obj = json.loads(foo)
```      

- foo - example JSON string
- obj - dictionary that will have JSON parsed and stored in it
- json.loads - parse a json string and saves in python dictionary

## Example:
```python
import json
foo = '{"id":"001","name":"abc","location":"xyz"}'
obj = json.loads(foo)
print(obj)
```
```bash
{'id': '001', 'name': 'abc', 'location': 'xyz'}
```

group: json
