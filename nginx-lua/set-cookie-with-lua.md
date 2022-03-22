# Set cookie with Lua

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.header['Set-Cookie'] = 'somecookie=abc; path=/'
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.header` - allows to set response headers
- `Set-Cookie` - we'll set this header to send new cookie to client
- `somecookie` - cookie name
- `abc` - cookie value
- `path=/` - cookie [path and other options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#syntax)

group: cookie

## Example: 
```nginx
ngx.header['Set-Cookie'] = 'somecookie=123; path=/'
```

