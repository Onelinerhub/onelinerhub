# How to log total time request took

```nginx
http {
  log_format test '[$time_local] $remote_addr: "$request" $request_time s';
  # ...
  
  server {
    # ...
    access_log /var/log/nginx/api.log api;
```

- $time_local - full date time of request
- $remote_addr - client IP address
- $request - full HTTP request string
- $request_time - time request took to process and return response (3 decimals)

group: log_times
