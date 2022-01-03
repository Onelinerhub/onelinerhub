# Find key by value in Redis

### This should be used for debugging purposes only:

```bash
for k in $(redis-cli KEYS '*'); do echo $k \"$(redis-cli GET $k)\"; done | grep "125"
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `KEYS '*'` - finds all keys on Redis server
- `do echo $k` - for every key we will print key name
- `redis-cli GET $k` - for every key we'll also get and print key value
- `grep "125"` - and then we'll filter by required value (`125` in our case)

## Example: 
```bash
for k in $(redis-cli KEYS '*'); do echo $k \"$(redis-cli GET $k)\"; done | grep "125"
```
```
test "125"
```

