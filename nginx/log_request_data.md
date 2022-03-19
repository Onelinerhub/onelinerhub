# Log requests (post and get)

```nginx
log_format data $request_body;

server {
  access_log /var/log/data.log data;
}
```

- `log_format` - defines new log format
- `data $request_body` - our log format will include only request body, named ```data```
- `/var/log/data.log data` - this will log all requests to ```/var/log/data.log``` with ```data``` format

group: log_format


