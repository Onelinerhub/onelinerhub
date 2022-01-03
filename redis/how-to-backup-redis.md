# How to backup Redis

```bash
redis-cli SAVE && cp /var/lib/redis/dump.rdb /var/backups/redis.rdb
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `SAVE` - syncs data file to disk file
- `/var/lib/redis/dump.rdb` - path to the Redis disk data file (use `redis-cli CONFIG GET dir` to locate it)
- `/var/backups/redis.rdb` - path to the backup file

group: backup


