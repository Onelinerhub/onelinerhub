# Calculating crc32

```nginx
server {
  location / {
    content_by_lua_block {
      local sign = ngx.crc32_long('Hi all')
    }
  }
}
```

- `ngx.crc32_long` - returns crc32 for specified string
- `'Hi all'` - string to calculate crc32 for
- `sign` - this variable will store generated crc32
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code

group: hashes

## Example: 
```nginx
local sign = ngx.crc32_long('Hi all')
ngx.say( sign )
```
```
2726312815

```

