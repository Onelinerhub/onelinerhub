# Convert table to string

### We'll use [cjson](https://luarocks.org/modules/openresty/lua-cjson) module to convert table to string representation:

```lua
local cjson = require "cjson"
str_table = cjson.encode(table)
```

- `require "cjson"` - load [lib:cjson](https://luarocks.org/modules/openresty/lua-cjson) module to work with JSON
- `str_table` - will convert string representation of a table
- `table` - table to convert to string
- `cjson.encode` - encode given object to JSON

group: convert_str

## Example: 
```lua
local cjson = require "cjson"
t={{1,2,3},{4,5,6}}
print(cjson.encode(t))
```
```
[[1,2,3],[4,5,6]]

```

