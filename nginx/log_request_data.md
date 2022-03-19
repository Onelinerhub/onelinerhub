# Log requests (post and get)

```nginx
log_format my_format '[$time_local] "$request"';

server {
  access_log /var/log/data.log my_format;
}
```

- `log_format` - defines new log format
- `data $request_body` - our log format will include only request body, named ```data```
- `/var/log/data.log data` - this will log all requests to ```/var/log/data.log``` with ```data``` format
- `my_format` - name of custom format to use
- `[$time_local] "$request"` - sample custom log format with time and request ([full ist of variables](http://nginx.org/en/docs/varindex.html))
- `/var/log/data.log` - path to log file

group: log_format


