# How to list all databases in Redis

```bash
redis-cli INFO keyspace
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `INFO` - get system information
- `keyspace` - will return information on available databases and their keys

## Example: 
```bash
redis-cli INFO keyspace
```
```
# Keyspace
db0:keys=4,expires=0,avg_ttl=0
```

