# How to set global variable

```nginx
init_by_lua_block {
  author = 'OLH'
}

server {
  location / {
    content_by_lua_block {
      ngx.say(author);
    }
  }
}
```


group: global

## Example: 
```nginx
ngx.say(author);
```
```
OLH

```

