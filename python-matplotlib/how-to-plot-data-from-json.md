# How to plot data from JSON

```python
import matplotlib.pyplot as plt
import json

dict = json.load(open('/var/www/examples/data.json', 'r'))

plt.plot(dict.keys(),dict.values())

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `json.load` - parses given JSON into dictionary
- `/var/www/examples/data.json` - path to a file to read JSON data from
- `.plot(` - plot specified data
- `dict.keys()` - returns JSON data keys as a list to use for `X` values
- `dict.values()` - returns JSON data values as a list to use for `Y` values
- `.show()` - render chart in a separate window

group: from

## Example: 
```python
import matplotlib.pyplot as plt
import json

with open('/var/www/examples/data.json', 'r') as f:
  print(f.read())

dict = json.load(open('/var/www/examples/data.json', 'r'))

plt.plot(dict.keys(),dict.values())

plt.show()
```
```
{"a":25,"b": 13,"c":45}


```

