# How to set Nginx variable

```nginx
server {
  location / {
    set_by_lua_block $test {
      return os.time()
    }
    
    return 200 $test;
  }
}
```

- `set_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive that sets specified variable with a result from Lua code
- `return os.time()` - sample Lua code that returns current unix timestamp
- `$test` - this variable will contain value returned by Lua code
- `return 200 $test;` - here we just send `$test` variable value to client 


