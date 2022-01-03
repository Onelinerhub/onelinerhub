# How to monitor commands on Redis server

### processlist
debug

```bash
redis-cli MONITOR
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `MONITOR` - will print all commands executed by the server in real time

## Example: 
```bash
redis-cli MONITOR
```
```
OK
1641234588.698650 [0 127.0.0.1:55798] "GET" "test"
1641234590.008590 [0 127.0.0.1:55800] "GET" "test1"
...
```

