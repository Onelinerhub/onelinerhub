# How to send plain text response

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.header["Content-type"] = 'text/plain'
      ngx.say('hi')
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.header` - allows to set response headers
- `text/plain` - set content type to `text/plain`
- `ngx.say` - output given text to client

group: response_content

## Example: 
```nginx
ngx.header["Content-type"] = 'text/plain'
ngx.say('hi')
```
```
hi

```

