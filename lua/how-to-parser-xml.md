# How to parser XML

```lua
local xml = require "xml"
local data = xml.load('<xml_string>')
```

- `require "xml"` - load [lib:xml](https://onelinerhub.com/lua/install-xml-module-with-luarocks) module to work with XML
- `xml.load` - parse given XML string and return object to access parsed data
- `'<xml_string>'` - sample XML string

group: xml

## Example: 
```lua
local xml = require "xml"
local data = xml.load [[
<?xml?>
<person>
  <name>Donald</name>
</person>
]]

local prop = xml.find(data, 'name')
print(prop[1])
```
```
Donald

```

