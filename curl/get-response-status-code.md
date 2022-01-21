# Get response status code

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://onelinerhub.com
```

- `curl` - base curl command
- `-o /dev/null` - will ask curl to skip response body
- `-s` - will not display any system information
- `-w` - will ask curl to display specified data about request
- `%{http_code}` - will output response code
- `https://onelinerhub.com` - sample URL to request


