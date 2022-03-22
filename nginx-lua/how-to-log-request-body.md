# How to log request body

```nginx
lua_need_request_body on;
log_format log_body '[$time_local] "$request" "$request_body"';

server {
  location / {
    content_by_lua 'ngx.say("ok")';
    access_log /var/log/nginx/lua.log log_body;
  }
}
```

- `lua_need_request_body` - ask Nginx to fill `$request_body` variable
- `log_format` - specify custom log format to log request body
- `$request_body` - this variable will contain request body
- `content_by_lua` - executed Lua script output will be sent to client
- `ngx.say("ok")` - just outputs `ok` so the client gets something in return
- `access_log` - set access log path and format
- `/var/log/nginx/lua.log` - path to access log

## Example: 
```nginx
curl localhost --data "test123"
tail /var/log/nginx/lua.log
```
```
[22/Mar/2022:16:15:22 +0000] "POST / HTTP/1.1" "test123"
```

