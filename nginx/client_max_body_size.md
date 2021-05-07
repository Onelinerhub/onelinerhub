# Increase request/upload size ("413 Request Entity Too Large" error)

```nginx
server {
  client_max_body_size 1G;
}
```

- client_max_body_size - this directive sets allowed size for a client request body
- 1G - we will limit requests to 1G
