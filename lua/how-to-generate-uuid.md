# How to generate UUID

```lua
local uuid = require("uuid")
local id = uuid()
```

- `require("uuid")` - load [UUID module](https://luarocks.org/modules/tieske/uuid)
- `local id` - will contain generated UUID
- `uuid()` - generates new UUID

## Example: 
```lua
local uuid = require("uuid")
print(uuid())
```
```
d764c8cc-e932-45c4-878d-7aa05d83f3ea

```

