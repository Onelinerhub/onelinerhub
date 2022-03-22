# Disable Lua code cache

### **Warning.** Disable code cache only for development purposes, don't use on production as it may reduce app performance.

```nginx
server {
  location / {
    lua_code_cache off;
    content_by_lua_file /path/to/script.lua;
  }
}
```

- `lua_code_cache` - controls Lua code caching
- `off` - disables code cache
- `content_by_lua_file` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) directive to load code from specified Lua code file
- `/path/to/script.lua` - path with Lua code to load

group: code_cahe


