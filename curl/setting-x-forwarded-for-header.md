# Setting "x-forwarded-for" header

```bash
curl -H "X-Forwarded-For: 1.2.3.4" https://example.org/
```

- `https://example.org/` - sample URL to send request to
- `-H` - sends specified header
- `1.2.3.4` - sample IP to set in `X-Forwarded-For` header


