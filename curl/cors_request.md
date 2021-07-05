# Send CORS request

```bash
curl -i -H "Origin: https://google.com" https://example.org
```

- -i - will include response headers in output
- -H - adds specified header to the request
- Origin: - will send origin url header (google.com in our case)
- example.org - example URL to call
