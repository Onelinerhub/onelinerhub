# How to parse YAML

```lua
local yml = require "lyaml"
local tbl = yml.load('sample: yaml')
```

- `require "lyaml"` - loads [lib:lyaml](https://onelinerhub.com/lua/install-yaml-lyaml-module-with-luarocks) module to work with YAML format
- `yml.load` - parses given YAML string and returns table
- `'sample: yaml'` - sample YAML string to parse
- `tbl` - resulting table with parsed data

group: yaml

## Example: 
```lua
local yml = require "lyaml"

local tbl = yml.load([[
people:
  name: Donald
]])

print(tbl.people.name)
```
```
Donald

```

link_youtube: https://youtu.be/jUl6vKw7UGY
