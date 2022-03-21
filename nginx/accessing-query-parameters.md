# Accessing query parameters

```nginx
server {
  location / {
    if ( $arg_something = test ) {
      return 403 sorry;
    }
  }
}
```

- `server {` - virtual server configuration block
- `location / {` - default location block
- `$arg_something` - gets `something` query string parameter value (e.g. `example.org/?something=test`)
- `test` - sample value to check against
- `return 403 sorry;` - return `403` header


