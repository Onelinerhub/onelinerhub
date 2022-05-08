# How to set Access-Control-Request-Headers header

```bash
curl https://example.org -X OPTIONS -H "Access-Control-Request-Headers: content-type"
```

- `curl` - base curl command
- `https://example.org` - sample URL to send OPTIONS request to
- `-X OPTIONS` - will send `OPTIONS` request
- `-H` - set specified header
- `content-type` - sets `Access-Control-Request-Headers` value to `content-type`

group: options


link_youtube: https://youtu.be/DvY5jdaO-Ys
