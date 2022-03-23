# Calculating md5

```nginx
server {
  location / {
    content_by_lua_block {
      local sign = ngx.md5('Hi all')
    }
  }
}
```

- `ngx.md5` - returns md5 for specified string
- `'Hi all'` - string to calculate md5 for
- `sign` - this variable will store generated md5
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code

group: hashes

## Example: 
```nginx
local sign = ngx.md5('Hi all')
ngx.say( sign )
```
```
c58716ce2c49b31ebfdc27266bcada91

```

