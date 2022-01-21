# Get SSL certificate info

```bash
curl -vvI https://google.com 2>&1 | awk 'BEGIN { cert=0 } /^\* SSL connection/ { cert=1 } /^\*/ { if (cert) print }'
```

- `curl` - base curl command
- `-vvI` - enables detailed info output
- `https://google.com` - domain to get SSL certificate of
- `2>&1` - redirect errors to standard output
- `awk` - manipulate strings (extract and filter in our case)
- `SSL connection` - find this substring in curl output and show everything after that


