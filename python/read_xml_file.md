# Read xml file

```python
from xml.dom import minidom
file = minidom.parse('/tmp/file.xml')
items = file.getElementsByTagName('item')
```

- `import minidom` - imports module to manipulate XML
- `minidom.parse(` - will parse specified XML file
- `'/tmp/file.xml'` - path to XML file
- `file.getElementsByTagName(` - return list of nodes by tag name

group: xml

