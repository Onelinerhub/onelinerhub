# How to set global variable

```nginx
init_by_lua_block {
  author = 'OLH'
}

server {
  location / {
    content_by_lua_block {
      ngx.say(author);
    }
  }
}
```

- `init_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to run specified Lua code on server startup
- `author` - this variable can be accessed globally
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client

group: global

## Example: 
```nginx
ngx.say(author);
```
```
OLH

```

