# How to save table to YAML

```lua
local yml = require "lyaml"
local yml_str = yml.dump({tbl})
```

- `require "lyaml"` - loads [lib:lyaml](https://onelinerhub.com/lua/install-yaml-lyaml-module-with-luarocks) module to work with YAML format
- `yml.dump` - converts given table into string
- `tbl` - sample table to convert to string
- `yml_str` - resulting string variable will contain YAML string

group: yaml

## Example: 
```lua
local yml = require "lyaml"
local tbl = {people={name="Donald"}}
print(yml.dump({tbl}))
```
```
---
people:
  name: Donald
...


```

link_youtube: https://youtu.be/S-YEozyNpBE
