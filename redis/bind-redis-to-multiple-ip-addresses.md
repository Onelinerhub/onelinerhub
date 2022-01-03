# Bind Redis to multiple IP addresses

### Edit `/etc/redis/redis.conf` Redis configuration file:

```yaml
bind 127.0.0.1 1.2.3.4
```

- `bind` - binds Redis server to specified IPs
- `127.0.0.1` - first IP to listen on
- `1.2.3.4` - second IP to listen on

group: conf


