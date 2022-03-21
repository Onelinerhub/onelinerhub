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
- `session` - sample value to match against cookies

group: if_else


