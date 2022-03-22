# Access args with Lua

```bash
server {
  location / {
    content_by_lua_block {
      ngx.say(ngx.var.arg_test)
    }
  }
}
```

- `server {` - virtual host configuration block
- `location` - specific location (group of URLs) configuration
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client 
- `ngx.var` - access request query string parameters
- `arg_test` - get `test` query string parameter value (e.g. `/?test=hi` will output `hi`)


