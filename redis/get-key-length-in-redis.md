# Get key length in Redis

```bash
echo $(redis-cli DEBUG OBJECT test) | cut -d' ' -f 5

```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `test` - key name to get length of
- `DEBUG OBJECT` - print internal data for specified key
- `cut -d' ' -f 5` - extract `serializedlength` key which print specified key length

## Example: 
```bash
echo $(redis-cli DEBUG OBJECT test) | cut -d' ' -f 5

```
```
serializedlength:3
```

