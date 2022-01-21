# How to set Origin of request

```bash
curl https://example.org -X OPTIONS -H "Origin: https://onelinerhub.com"
```

- `curl` - base curl command
- `https://example.org` - sample URL to send OPTIONS request to
- `-X OPTIONS` - will send `OPTIONS` request
- `-H` - set specified header
- `https://onelinerhub.com` - set this value as an Origin for request

group: options


