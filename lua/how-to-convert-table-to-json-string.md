# How to convert table to JSON string

### We'll use [lib:cjson](https://onelinerhub.com/lua/install-cjson-module-with-luarocks) module to convert table to string representation:

```lua
local cjson = require "cjson"
local json_str = cjson.encode(tbl)
```

- `require "cjson"` - load [lib:cjson](https://onelinerhub.com/lua/install-cjson-module-with-luarocks) module to work with JSON
- `cjson.encode` - encodes given table to JSON string
- `tbl` - table to encode to JSON string
- `json_str` - resulting JSON string

group: json

## Example: 
```lua
local cjson = require "cjson"
local tbl = {name="Donald"}
local str = cjson.encode(tbl)
print(str)
```
```
{"name":"Donald"}

```

