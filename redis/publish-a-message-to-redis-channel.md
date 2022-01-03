# Publish a message to Redis channel

```bash
redis-cli PUBLISH some message
```

- `redis-cli` - executes Redis command in bash
- `PUBLISH` - send message to the specified channel
- `some` - name of the channel (just a string) which we want to publish message to
- `message` - our message to publish

group: pub_sub

## Example: 
```bash
redis-cli PUBLISH test hi
```
```
(integer) 1
```

