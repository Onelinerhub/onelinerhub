# How to validate xml

```python
import xmlschema

try:
  xmlschema.validate('file.xml', 'schema.xsd')
  print('XML is valid')
except:
  print('XML is invalid')
```

- `xmlschema` - XML validator module, [more info](https://pypi.org/project/xmlschema/)
- `xmlschema.validate(` - validate given XML file with given XML schema
- `file.xml` - XML file to validate
- `schema.xsd` - Schema to use for validation

