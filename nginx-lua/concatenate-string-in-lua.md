# Concatenate string in Lua

```nginx
server {
  location / {
    content_by_lua_block {
      local str1 = "Hi "
      local str2 = "All!"
      ngx.say(str1 .. str2)
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `local str1` - defines first string
- `local str2` - defines second string
- `str1 .. str2` - concatenates `str1` and `str2`

group: string

## Example: 
```nginx
local str1 = "Hi "
local str2 = "All!"
ngx.say(str1 .. str2)
```
```
Hi All!

```

