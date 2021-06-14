# Restore dump created by mysqldump

```bash
mysql db < backup.sql
```

- db - database name to load dump for (can be skipped if the ```backup.sql``` is dumped for several databases)
- backup.sql - name of dump created by mysqldump

group: dump
