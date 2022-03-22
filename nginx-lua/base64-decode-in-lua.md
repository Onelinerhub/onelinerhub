# Base64 decode in Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local enc = ngx.decode_base64('dmFsdWU=')
      ngx.say(enc)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.decode_base64` - decode given value from base64
- `dmFsdWU=` - sample base64-encoded value to decode
- `ngx.say` - output given text to client

group: base64


