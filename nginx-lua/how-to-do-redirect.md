# How to do redirect

```nginx
server {
  location / {
    content_by_lua_block {
      return ngx.redirect("/new_page.html")
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.redirect` - redirect to other page (with `302` status code)
- `/new_page.html` - URL to redirect to

group: redirect


