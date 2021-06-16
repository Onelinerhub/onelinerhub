# Create innodb tables dump without locking tables

```bash
mysqldump --single-transaction=TRUE > backup.sql
```

- single-transaction - will execute a transaction (thus, consistent state of all tables) instead of locking innodb tables
- backup.sql - name of dump file

group: nolock_dump
