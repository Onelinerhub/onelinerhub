# Create innodb tables dump without locking tables

```bash
mysqldump --single-transaction=TRUE
```

- single-transaction - will execute a transaction (thus, consistent state of all tables) instead of locking innodb tables

group: nolock_dump
