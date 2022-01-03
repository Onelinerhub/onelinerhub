# Get all keys of list in Redis

```bash
redis-cli lrange lst 0 -1
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `lrange` - returns all elements of a list within specified range
- `lst` - name of the list to get elements from
- `0 -1` - will return all elements of the selected list

group: lists


