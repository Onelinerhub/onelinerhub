# Using if else condition

### Here we use temporary `$test` variable to emulate `if-else` functionality as Nginx doesn't support `else`:

```nginx
server {
  set $test "notok";
  if ($http_cookie ~* "session") {
    set $test "ok";
  }
  
  if ($test = "ok") {
    return 200;
  }
  
  if ( $test = "notok" ) {
    return 403;
  }
}
```

- `set $test "notok"` - set default value for `$test` variable
- `if ($http_cookie ~* "session")` - condition which we need `else` functionality for
- `set $test "ok"` - set `ok` value if condition is `true`
- `if ($test = "ok") {` - this condition will repeat our original condition to check
- `if ( $test = "notok" ) {` - this condition will pass if previous condition didn't pass - so the same as `else` functionality

group: if_else


