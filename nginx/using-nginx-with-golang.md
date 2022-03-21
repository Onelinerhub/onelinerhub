# Using Nginx to serve Golang app

```nginx
server {
  location / {
    proxy_pass http://localhost:9991;
  }
}
```

- `server {` - virtual server configuration block
- `location / {` - default location block
- `proxy_pass` - send this request to the following upstream (other server)
- `localhost:9991` - host and port that our Golang app is listening to


