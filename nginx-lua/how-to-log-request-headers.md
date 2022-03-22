# How to log request headers

```nginx
log_format log_hdrs '[$time_local] "$request" "$req_hdr"';

server {
  location / {
    set_by_lua_block $req_hdr {
      return ngx.req.get_headers()['Accept']
    }
    
    access_log /var/log/nginx/lua.log log_hdrs;
  }
}
```

- `log_format` - specify custom log format to log request body
- `log_hdrs` - access log format name with request header
- `$req_hdr` - this variable will contain specific request header value
- `set_by_lua_block` - [lib:nginx-lua](/nginx-lua/how-to-install-nginx-lua-module-in-ubuntu-ubuntuversion) module directive that sets specified variable with a result from Lua code
- `ngx.req.get_headers()` - returns table with request headers
- `Accept` - sample HTTP header to log value of
- `access_log` - set access log path and format
- `/var/log/nginx/lua.log` - path to access log

group: log

## Example: 
```nginx
curl localhost
tail /var/log/nginx/lua.log
```
```
[22/Mar/2022:16:26:08 +0000] "GET /hdrs HTTP/1.1" "*/*"
```

