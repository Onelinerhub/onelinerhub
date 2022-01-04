# Redis URI with password example

### URIs are used in [connections by URL](/python-redis/connecting-to-redis-with-fromurl):

```txt
redis://user:pwd@1.2.3.4:6379/0
```

- `redis://` - redis protocol
- `user:pwd` - username and password for authentication
- `1.2.3.4` - IP address of the Redis host
- `6379` - Redis port to connect to
- `/0` - select first (`0`) database

group: uri


