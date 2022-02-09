# Sending keep alive request

```bash
curl -H "Connection: keep-alive" -H "Keep-Alive: timeout=5, max=100" https://example.org
```

- `-H` - sets specified header
- `Connection: keep-alive` - use keep-alive connection
- `Keep-Alive:` - specify keep-alive connection settings
- `timeout=5` - timeout for request is limited to `5` seconds
- `max=100` - limits number of requests per connection to 100


