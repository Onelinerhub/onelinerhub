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


group: cookie

## Example: 
```nginx
ngx.header['Set-Cookie'] = 'somecookie=123; path=/'
```

