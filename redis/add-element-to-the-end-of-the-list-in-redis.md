# Add element to the end of the list in Redis

```bash
redis-cli rpush lst hi
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `rpush` - adds element to the end of the list
- `lst` - name of the list to add element to
- `hi` - value of the element to add

group: lists

## Example: 
```bash
redis-cli lpush lst hi
```
```
(integer) 4
```

