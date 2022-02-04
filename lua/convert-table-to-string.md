# Convert table to string

### We'll use [lib:cjson](https://onelinerhub.com/lua/install-cjson-module-with-luarocks) module to convert table to string representation:

```bash
local cjson = require "cjson"
str_table = cjson.encode(table)
```

- `require "cjson"` - load [lib:cjson](https://onelinerhub.com/lua/install-cjson-module-with-luarocks) module to work with JSON
- `str_table` - will convert string representation of a table
- `table` - table to convert to string
- `cjson.encode` - encode given object to JSON

group: convert_str

## Example: 
```bash
local cjson = require "cjson"
t={{1,2,3},{4,5,6}}
print(cjson.encode(t))
```
```
[[1,2,3],[4,5,6]]

```

