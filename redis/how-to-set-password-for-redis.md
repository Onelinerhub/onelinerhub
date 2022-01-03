# How to set password for Redis

### Edit `/etc/redis/redis.conf` Redis configuration file (and don't forget to [restart Redis](/redis/how-to-restart-redis-on-ubuntu-ubuntuversion) after that):

```bash
requirepass strong0pwd
```

- `requirepass` - set specify password to authenticate Redis
- `strong0pwd` - sample password to set

group: password


