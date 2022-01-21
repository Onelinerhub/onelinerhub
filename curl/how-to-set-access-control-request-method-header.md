# How to set Access-Control-Request-Method header

```bash
curl https://example.org -X OPTIONS -H "Access-Control-Request-Method: POST"
```

- `curl` - base curl command
- `https://example.org` - sample URL to send OPTIONS request to
- `-X OPTIONS` - will send `OPTIONS` request
- `-H` - set specified header
- `POST` - sets `Access-Control-Request-Method` value to `POST`

group: options


