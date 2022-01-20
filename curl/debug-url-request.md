# Debug URL request

```bash
curl -v https://google.com
```

- `curl` - base curl command
- `-v` - verbose mode enabled
- `https://google.com` - sample URL to debug request to

## Example: 
```bash
curl -v https://google.com
```
```
*   Trying 142.250.203.206:443...
* Connected to google.com (142.250.203.206) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
...
```

