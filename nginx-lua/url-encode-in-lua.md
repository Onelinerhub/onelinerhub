# Url encode in Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say( ngx.escape_uri('hi all') )
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.escape_uri` - encodes given string to URL-encoded form
- `'hi all'` - sample string to encode
- `ngx.say` - output given text to client

group: urlencode

## Example: 
```nginx
ngx.say( ngx.escape_uri('hi all') )
```
```
hi%20all

```

