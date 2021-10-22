# How to parse json

```python
import json

#example json string
foo = '{"id":"001","name":"abc","location":"xyz"},{"id":"002","name":"def","location":"uvw"}'
json.loads(foo) #for json string

file1=open('data.json',)
foo1 = json.load(file1)
file1.close()
```      

- json.loads(string) - parse a json string and saves in python dictionary
- json.load(file_name) - parse json object in file and gives result in dictionary