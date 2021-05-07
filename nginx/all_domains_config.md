# Catch all domains with one config

```nginx
server {
  listen 80 default_server;
}
```

- default_server - lets nginx know that this ```server``` block should catch all requests for unknown domains
