# Create myisam tables dump without locking tables

```bash
mysqldump --lock-tables=false > backup.sql
```

- lock-tables=false - will disable lock for myisam tables (but this can lead to inconsistent table data in a dump file)
- backup.sql - name of dump file

group: nolock_dump
