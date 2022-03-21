# Proxy gRPC traffic with Nginx

```nginx
 server {
  listen 80 http2;

  location / {
    grpc_pass grpc://1.2.3.4:50051;
  }
}
```

- `server {` - virtual server configuration block
- `listen 80 http2` - gRPC is transported within `HTTP/2` protocol
- `grpc_pass` - will pass gRPC traffic to the specified gRPC server
- `1.2.3.4:50051` - gRPC host / port to proxy traffic to

group: proxy


