# How to return file for download

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.header["Content-type"] = 'text/csv'
      ngx.header["Content-Disposition"] = 'attachment; filename="test.csv"'
      ngx.say("1,2,3")
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.header` - allows to set response headers
- `Content-type` - response header to set
- `Content-Disposition` - this header will force content download instead of output to browser
- `test.csv` - this file name will be used for download
- `ngx.say` - output given text to client
- `"1,2,3"` - example content for download

## Example: 
```nginx
ngx.header["Content-type"] = 'text/csv'
ngx.header["Content-Disposition"] = 'attachment; filename="test.csv"'
ngx.say("1,2,3")
```
```
1,2,3

```

