# How to check if response if HTTP2

### This code will return HTTP version of the response:

```bash
curl -o /dev/null -s -w "%{http_version}\n" https://onelinerhub.com
```

- `curl` - base curl command
- `-o /dev/null` - will ask curl to skip response body
- `-s` - will not display any system information
- `-w` - will ask curl to display specified data about request
- `https://onelinerhub.com` - sample URL to request
- `http_version` - will return HTTP protocol version

group: http_version

## Example: 
```bash
curl -o /dev/null -s -w "%{http_version}\n" https://onelinerhub.com
```
```
2
```

