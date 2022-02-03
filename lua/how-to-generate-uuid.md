# How to generate UUID

```lua
local socket = require("socket")
local uuid = require("uuid")
uuid.seed()
local id = uuid()
```

- `require("uuid")` - load [UUID module](https://luarocks.org/modules/tieske/uuid)
- `local id` - will contain generated UUID
- `uuid()` - generates new UUID
- `require("socket")` - loads socket lib to seed UUID random generator
- `uuid.seed()` - seed random generator to get unique UUID values on each call

## Example: 
```lua
local socket = require("socket")
local uuid = require("uuid")
uuid.seed()
print(uuid())
print(uuid())
print(uuid())
```
```
08dcc56c-82d6-4b63-a2d6-8ca1028ae59d
89f6e0f9-c38a-41e0-a986-4cd488eedd91
cba3fd4e-7938-429c-8f3f-3d12c923af53

```

