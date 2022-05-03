# How to convert table to XML string

```lua
local xml = require "xml"
local xml_string = xml.dump(tbl)
```

- `require "xml"` - load [lib:xml](https://onelinerhub.com/lua/install-xml-module-with-luarocks) module to work with XML
- `xml.dump` - converts given table to XML string
- `tbl` - sample table to convert to XML string
- `xml_string` - resulting string with XML

group: xml

## Example: 
```lua
local xml = require "xml"
local tbl = {xml = 'person', name="Donald"}
local xml_string = xml.dump(tbl)
print(xml_string)
```
```
<person name='Donald'/>

```

link_youtube: https://youtu.be/MI-X46pWEoU
