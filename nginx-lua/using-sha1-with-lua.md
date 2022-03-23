# Using sha1 with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local sign = ngx.sha1_bin('Hi all')
    }
  }
}
```

- `ngx.sha1_bin` - returns sha1 for specified string
- `'Hi all'` - string to calculate sha1 for
- `sign` - this variable will store generated sha1

group: hashes

## Example: 
```nginx
local sign = ngx.sha1_bin( 'Hi all')
ngx.say( ngx.encode_base64(sign) )
```
```
faKqkNyx5BIvCpDHYdqTb/LtxVc=

```

