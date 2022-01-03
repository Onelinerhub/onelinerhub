# How to ping Redis server for health

```bash
redis-cli PING
```

- `redis-cli` - executes Redis command in bash
- `PING` - send `PING` to the server, which should answer `PONG` in response

## Example: 
```bash
redis-cli PING
```
```
PONG
```

## Additional keywords
- health check
- healthcheck

