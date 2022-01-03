# Sample Redis usage

```bash
redis-cli SET test 123
redis-cli GET test
```

- `redis-cli` - executes Redis command in bash
- `SET` - sets value by specified key
- `test` - key to set (and the get) value
- `123` - value to set
- `GET` - gets value by key

## Example: 
```bash
redis-cli SET test 123
redis-cli GET test
```
```
OK
"123"
```

