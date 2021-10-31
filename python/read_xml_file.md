# Read xml file

```python
import xml.etree.ElementTree as ET
tree = ET.parse('folder/file.xml')
root = tree.getroot()

for element in root:
    for subelement in element:
        print(subelement.text)
```

- `import xml.etree.ElementTree as ET` - this module implements a simple and efficient API for parsing and creating XML data (ET in short);
- `ElementTree` class represents the whole XML document as a tree;
- `tree` - an element tree;
- `parse` - function that parses an XML section into an element tree;
- `'folder/file.xml'` - the path to source file ("XML section") we are parsing;
- `root` - the root element;
- `getroot()` - function that returns the root element for given tree;
- `element` - first level of nesting of tags in the source file;
- `subelement` - second level of nesting of tags in the source file;
- `text` - attribute holds either the text between the subelement’s start tag and its first child or end tag;
- `print(subelement.text)` - print result.

## Example:
*friends.xml:*
```xml
<data>
    <friend name="Paul">
        <hobby>Playing computer games</hobby>
    </friend>
    <friend name="Dorothy">
        <hobby>Swimming</hobby>
    </friend>
</data>
```
*read_xml_py:*
```python
import xml.etree.ElementTree as ET
tree = ET.parse('friends.xml')
root = tree.getroot()

for child in root:
    print("Tag:", child.tag,"\n", "Attribute", child.attrib, "\n", "Text:", child.text)
    for element in child:
        print("Tag:", element.tag, "\n", "Attribute:", element.attrib, "\n", "Text:", element.text)

```

- `tag` - a string identifying what kind of data this element represents (the element type, in other words);
- `attrib` - a dictionary containing the element’s attributes.

*result:*
```bash
Tag: friend
 Attribute {'name': 'Paul'}
 Text:

Tag: hobby
 Attribute: {}
 Text: Playing computer games
Tag: friend
 Attribute {'name': 'Dorothy'}
 Text:

Tag: hobby
 Attribute: {}
 Text: Swimming

```
