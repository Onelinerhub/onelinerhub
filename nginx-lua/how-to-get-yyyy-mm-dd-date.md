# How to get YYYY-MM-DD date

```nginx
server {
  location / {
    content_by_lua_block {
      local date = os.date("!%Y-%m-%d")
      ngx.say(date)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `os.date` - returns date/time in a given format
- `ngx.say` - output given text to client

group: time

## Example: 
```nginx
ngx.say(os.date("!%Y-%m-%d"))
```
```
2022-03-22

```

