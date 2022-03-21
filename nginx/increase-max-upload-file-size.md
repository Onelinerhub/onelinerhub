# Increase max upload file size

```nginx
server {
  client_max_body_size 2G;
}
```

- `server {` - virtual server configuration block
- `client_max_body_size` - this directive sets allowed size for a client request body (including upload file size)
- `2G` - allow uploading up to 2G files


