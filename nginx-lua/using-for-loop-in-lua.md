# How to use for loop

```nginx
server {
  location / {
    content_by_lua_block {
      for i = 1,10,1
      do 
        ngx.say(i)
      end
    }
  }
}
```

- `content_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive to specify block of Lua code
- `for i = 1,10,1` - for loop from `1` to `10` with increment step of `1`
- `ngx.say` - output given text to client

## Example: 
```nginx
for i = 1,10,1
do 
  ngx.say(i)
end
```
```
1
2
3
4
5
6
7
8
9
10

```

