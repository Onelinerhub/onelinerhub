# How to sleep in code

```nginx
server {
  location / {
    content_by_lua_block {
      ngx.say(os.time())
      os.execute('sleep 1')
      ngx.say(os.time())
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `ngx.say` - output given text to client
- `os.execute` - executes given shell command
- `'sleep 1'` - shell command to sleep for `1` second

## Example: 
```nginx
ngx.say(os.time())
os.execute('sleep 1')
ngx.say(os.time())
```
```
1648048276
1648048277

```

