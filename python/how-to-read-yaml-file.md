# How to read yaml file

```python
import yaml

with open('file.yml') as f:
  data = yaml.load(f)
```

- `import yaml` - import library to work with YAML
- `'file.yml'` - path to our YAML file
- `yaml.load` - loads YAML from file and parses it into dictionary
- `data` - this dictionary will store parsed data

## Example: 
```python
import yaml

with open('/var/www/examples/file.yml') as f:
  data = yaml.load(f)

print(data)
```
```
{'test': {'var1': 12, 'var2': 43}}

```

## Additional keywords
- parse
- open
