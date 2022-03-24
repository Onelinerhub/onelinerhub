# How to use Luarocks and other modules in Nginx Lua

### After installation of [Luarocks](https://luarocks.org/) module, we need to add its include path into Nginx Lua environment:

```nginx
lua_package_path "/usr/local/share/lua/5.3/?.lua;";

init_by_lua_block {
  uuid = require("uuid")
}

server {
  location / {
    content_by_lua_block {
      local id = uuid()
    }
  }
}
```

- `lua_package_path` - specify include path for Lua modules
- `/usr/local/share/lua/5.3/` - possible path to Luarocks installed modules ([find your own path](/lua/how-to-find-luarocks-module-path))
- `init_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to run specified Lua code on server startup
- `require("uuid")` - loads UUID Luarocks module
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `local id = uuid()` - [UUID module](https://luarocks.org/modules/tieske/uuid) sample usage


