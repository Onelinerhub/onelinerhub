# Get memory usage of a key in Redis

```bash
redis-cli info memory | grep used_memory_human:
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `info memory` - returns stats on memory usage
- `used_memory_human` - filter only information on currently used memory

group: mem

## Example: 
```bash
redis-cli info memory | grep used_memory_human:
```
```
used_memory_human:862.28K
```

