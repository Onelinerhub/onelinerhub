# How to get Redis logs

```bash
redis-cli CONFIG GET logfile
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `CONFIG GET` - returns value of the specified config parameter
- `logfile` - returns path to the server logs file

## Example: 
```bash
redis-cli CONFIG GET logfile
```
```
1) "logfile"
2) "/var/log/redis/redis-server.log"
```

## Additional keywords
- find
- locate

