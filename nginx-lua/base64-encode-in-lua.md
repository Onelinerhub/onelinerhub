# Base64 encode in Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local enc = ngx.encode_base64('value')
      ngx.say(enc)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.encode_base64` - encode given value into base64
- `value` - sample value to encode
- `ngx.say` - output given text to client

group: base64

## Example: 
```nginx
curl "http://lua.onelinerhub.com/base64"
```
```
dmFsdWU=
```

