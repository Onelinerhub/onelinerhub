# How execute shell command with Lua

### If you want to capture command output, you should use [`io.opepn`](/nginx-lua/executing-commands-with-iopopen-in-lua) instead.

```nginx
server {
  location / {
    content_by_lua_block {
      os.execute('echo 1 > /tnp/hi')
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `os.execute` - executes given shell command
- `echo 1 > /tnp/hi` - random shell command

group: shell

## Example: 
```nginx
os.execute('echo 1 > /tmp/hi')
ngx.say('ok')
```
```
ok

```

