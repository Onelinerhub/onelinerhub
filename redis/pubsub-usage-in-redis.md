# Pub/sub usage in Redis

```bash
redis-cli SUBSCRIBE some
```

- `redis-cli` - executes Redis command in bash
- `SUBSCRIBE` - receive message from the specified channel
- `some` - name of the channel (just a string) which messages are going to be [published to]()

group: pub_sub

## Example: 
```bash
redis-cli SUBSCRIBE test
```
```
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "test"
3) (integer) 1
1) "message"
2) "test"
3) "hi"
...
```

