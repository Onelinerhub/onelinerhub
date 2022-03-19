# Using proxy_redirect

```nginx
server {
  location /new/ {
    proxy_pass http://localhost:81/old/;
    proxy_redirect http://localhost:81/old/ /new/;
  }
}
```

- `server {` - virtual server configuration block
- `http://localhost:81/old/` - sample backend to use to proxy
- `/new/` - replace `Location` header from proxy backend by this URI (will use same server name and port)


