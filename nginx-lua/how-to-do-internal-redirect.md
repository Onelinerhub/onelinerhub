# How to do internal redirect

```nginx
server {
  location /test {
   content_by_lua_block {
      ngx.exec("@files")
   }
  }
  
  location @files {
   content_by_lua_block {
    ngx.say('helo after internal redirect')
   }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.exec` - does internal redirect to other Nginx location
- `@files` - named location to redirect internally to
- `ngx.say` - output given text to client

group: redirect


