# How to do URL decode

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say( ngx.unescape_uri('hi%20all') )
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.unescape_uri` - decodes given string from URL-encoded form
- `hi%20all` - sample string to decode
- `ngx.say` - output given text to client

group: urlencode

## Example: 
```nginx
ngx.say( ngx.unescape_uri('hi%20all') )
```
```
hi all

```

