# Using if..else

```nginx
server {
  location / {
    content_by_lua_block {
      local a = 2
      if a == 1 then
        ngx.say('first')
      elseif a == 2 then
        ngx.say('second')
      else
        ngx.say('other')
      end
    }
  }
}
```

- `if a == 1 then` - check first condition and execute code below
- `elseif a == 2 then` - if first condition is `false`, check second condition
- `end` - conditions block should end with `end`
- `ngx.say('other')` - default code to execute if all conditions are `false`

## Example: 
```nginx
local a = 2
if a == 1 then
  ngx.say('first')
elseif a == 2 then
  ngx.say('second')
else
  ngx.say('other')
end
```
```
second

```

