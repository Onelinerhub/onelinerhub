# How to echo with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say('hi')
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `'hi'` - sample text to output to client

## Example: 
```nginx
ngx.say('hi')
```
```
hi

```

