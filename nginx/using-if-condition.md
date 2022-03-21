# Using if condition

```nginx
server {
  if ($http_cookie ~* "session") {
    set $test "ok";
  }
}
```

- `server {` - virtual server configuration block

group: if_else


