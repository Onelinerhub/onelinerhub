# Sending request with query string from terminal

```bash
curl "https://onelinerhub.com/search?q=clickhouse&p=2"
```

- `curl` - base curl command
- `"` - use quotes to send query strings safely
- `?q=` - quotes (`"`) will safely allow to send `?` and `&` symbols


