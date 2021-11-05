# How to parse xml

```python
from xml.dom import minidom
parsed = minidom.parseString(xml_string)
```

- `parsed` - will contain parsed XML object
- `parseString` - parses specified XML string
- `import minidom` - import module to manipulate XML
- `xml_string` - XML string to parse

group: xml

## Example: 
```python
from xml.dom import minidom
parsed = minidom.parseString('<item>hi</item>')
print(parsed.getElementsByTagName('item')[0].firstChild.nodeValue)
```
```
hi

```
