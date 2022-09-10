# How to do 301 redirect

### Want to do [302 redirect](/nginx-lua/how-to-do-redirect)?

```nginx
server {
  location / {
    content_by_lua_block {
      return ngx.redirect("/new_page.html", 301)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.redirect` - redirect to other page
- `/new_page.html` - URL to redirect to
- `301` - status code to use for redirect

group: redirect


link_youtube: https://youtu.be/5aG6AYG6d7Y
