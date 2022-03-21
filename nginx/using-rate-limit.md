# Using rate limit

```nginx
limit_req_zone $binary_remote_addr zone=my_lim:60m rate=5r/s;
 
server {
  location / {
    limit_req zone=my_lim;
  }
}
```

- `limit_req_zone` - define requests limiting rules
- `$binary_remote_addr` - key to use for request limiting, client IP address in our case 
- `my_lim` - name of this request limits rule (zione)
- `60m` - size in memory to store request frequency for IP addresses, `60m` will allow storing around 1 million IP addresses 
- `5r/s` - rate limit (5 requests per second)
- `server {` - virtual server configuration block
- `location / {` - default location block
- `limit_req zone=my_lim` - specify rate limit zone to use (`my_lim` zone in our case)


