# CORS header to allow all origins

```nginx
server {
  add_header "Access-Control-Allow-Origin" $http_origin;
}
```

- add_header - sets specified header
- Access-Control-Allow-Origin - set CORS header to control access from origins
- $http_origin - always set to specified origin (thus, allow access for any origin)
