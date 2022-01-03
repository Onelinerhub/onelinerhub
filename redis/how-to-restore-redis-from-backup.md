# How to restore Redis from backup

### Let's assume our backup is located in `/var/backups/redis.rdb`, then we just need to copy it back (while the Redis server is stopped) and start Redis server:

```bash
systemctl stop redis && mv /var/backups/redis.rdb /var/lib/redis/dump.rdb && systemctl start redis
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `stop redis` - stops Redis server
- `/var/lib/redis/dump.rdb` - path to the Redis disk data file (use `redis-cli CONFIG GET dir` to locate it)
- `/var/backups/redis.rdb` - path to the backup file
- `start redis` - starts Redis server

group: backup


