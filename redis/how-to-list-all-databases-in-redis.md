# How to show databases count in Redis

```bash
redis-cli CONFIG GET DATABASES
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `CONFIG GET` - returns value of the specified config parameter
- `DATABASES` - total count of databases that can be used

group: dbs

## Example: 
```bash
redis-cli CONFIG GET DATABASES
```
```
1) "databases"
2) "16"
```

