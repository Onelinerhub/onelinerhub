# Set key with expiration in Redis

```bash
redis-cli SET test 124 EX 300
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `SET` - sets value by specified key
- `test` - key name to set value for
- `124` - value to set for specified key
- `EX` - set seconds to expire after for the key
- `300` - our key will expire in 300 seconds

group: keys

## Example: 
```bash
redis-cli SET test 124 EX 5
redis-cli GET test
sleep 6
redis-cli GET test
```
```
OK
"124"
(nil)

```

