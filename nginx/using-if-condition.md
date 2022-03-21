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
- `if (` - checks specified rule
- `set $test "ok";` - set `$test` variable if rule is `true`

group: if_else


