# How to convert unix timestamp to date time

```nginx
server {
  location / {
    content_by_lua_block {
      local date_time = os.date("!%Y-%m-%d %H:%M", 1647900352)
      ngx.say(date_time)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `os.date` - returns date/time in a given format
- `1647900352` - pass unix timestamp as a second argument
- `ngx.say` - output given text to client

group: time

## Example: 
```nginx
ngx.say(os.date("!%Y-%m-%d %H:%M", 1647900352))
```
```
2022-03-21 22:05

```

