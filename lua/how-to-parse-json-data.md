# How to parse JSON data

### We'll use [lib:cjson](https://onelinerhub.com/lua/install-cjson-module-with-luarocks) module to convert table to string representation:

```lua
local cjson = require "cjson"
tbl = cjson.decode('{"name":"Donald"}')
```

- `require "cjson"` - load [lib:cjson](https://onelinerhub.com/lua/install-cjson-module-with-luarocks) module to work with JSON
- `cjson.decode` - decodes given JSON string to table
- `tbl` - table will contain decoded data from JSON string

group: json

## Example: 
```lua
local cjson = require "cjson"
tbl = cjson.decode('{"name":"Donald"}')
print(tbl.name)
```
```
Donald

```

