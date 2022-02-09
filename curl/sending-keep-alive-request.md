# Sending keep alive request

```bash
curl -H "Connection: keep-alive" -H "Keep-Alive: timeout=10, max=100" https://example.org
```

- `-H` - sets specified header
- `Connection: keep-alive` - use keep-alive connection
- `Keep-Alive:` - specify keep-alive connection settings
- `timeout=10` - server will wait up to `10` seconds before closing keep-alive connection
- `max=100` - limits number of requests to 100 before closing connection


