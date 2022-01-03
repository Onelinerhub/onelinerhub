# Find Redis server port

```bash
redis-cli info | grep port
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `info` - get system info
- `grep port` - filter only server port information

## Example: 
```bash
redis-cli info | grep port
```
```
tcp_port:6379
```

