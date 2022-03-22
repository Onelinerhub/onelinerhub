# How to access environment variables

```nginx
env PATH;

http {
  #...
  
  server {
    location / {
      content_by_lua_block {
        ngx.say(os.getenv("PATH"))
      }
    }
  }
}
```

- `env PATH` - we need to add `env` directive to core Nginx config to access needed environment variables (`PATH` in our case)
- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `os.getenv` - get specified environment variable value
- `PATH` - sample environment variable to get value of


