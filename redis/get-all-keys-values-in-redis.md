# Get all keys values in Redis

```bash
for k in $(redis-cli KEYS '*'); do echo $k \"$(redis-cli GET $k)\"; done
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `KEYS '*'` - finds all keys on Redis server
- `do echo $k` - for every key we will print key name
- `redis-cli GET $k` - for every key we'll also get and print key value

group: find


