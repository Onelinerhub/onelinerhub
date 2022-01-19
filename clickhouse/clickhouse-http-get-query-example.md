# Clickhouse HTTP GET query example

```bash
curl "127.0.0.1:8123?query=select+now()"
```

- `curl` - use curl to send HTTP request
- `127.0.0.1` - Clickhouse host IP
- `8123` - Clickhouse server port
- `query` - send SQL query in `query` parameter
- `select+now()` - URL-encoded SQL query

group: http

## Example: 
```bash
curl "127.0.0.1:8123?query=select+now()"
```
```
2022-01-12 19:02:22
```

link_youtube: https://youtu.be/y6q4pneKyu8
