# Using if condition

```nginx
server {
  if ($http_cookie ~* "session") {
    set $test "ok";
  }
}
```

- `server {` - virtual server configuration block
- `$http_cookie` - variable to access cookie values

group: if_else


