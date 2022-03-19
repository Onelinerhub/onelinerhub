# How to log in JSON format

```nginx
log_format json escape=json
  '{'
    '"time_local":"$time_local",'
    '"remote_addr":"$remote_addr",'
    '"request":"$request",'
    '"status": "$status",'
    '"body_bytes_sent":"$body_bytes_sent",'
    '"http_referrer":"$http_referer"'
  '}';

server {
  access_log /var/log/nginx/json.log json;
}
```

- `log_format json` - define custom log format for json
- `escape=json` - rule to escape values
- `/var/log/nginx/json.log` - path to JSON access log
- `json;` - sets specified format for log (`json` in our case)

## Example: 
```nginx
tail /var/log/nginx/json.log
```
```
{"time_local":"19/Mar/2022:20:44:10 +0200","remote_addr":"31.0.73.130","request":"GET / HTTP/2.0","status": "200","body_bytes_sent":"1683","http_referrer":""}

```

