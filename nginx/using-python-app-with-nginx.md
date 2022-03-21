# Using python app with Nginx

```nginx
server {
  location / {
    proxy_pass http://localhost:9992;
  }
}
```

- `server {` - virtual server configuration block
- `location / {` - default location block
- `proxy_pass` - send this request to the following upstream (other server)
- `localhost:9992` - host and port that our Python app is listening to


