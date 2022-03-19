# How to limit allowed query string size

### As query string is a part of client headers, this can be controlled via changing buffers used for reading client headers:

```nginx
server {
  large_client_header_buffers 4 8k;
}
```

- `server {` - virtual server configuration block
- `large_client_header_buffers` - configure buffers to use for reading client headers
- `4 8k` - use `4` buffers `8k` each to read headers


