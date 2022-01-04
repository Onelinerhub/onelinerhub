# Configure Redis to use unix socket

### Edit `/etc/redis/redis.conf` Redis configuration file:

```yml
unixsocket /var/run/redis/redis-server.sock
unixsocketperm 775
```

- `unixsocket` - path to the unix socket file (be sure to create the corresponding directory)
- `unixsocketperm` - unix socket permissions (`775` in our case)

group: conf


