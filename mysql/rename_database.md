# Rename database

```bash
mysql -e "CREATE DATABASE newdb"
mysqldump db | mysql newdb
```

- CREATE DATABASE newdb - creates new database named ```newdb```
- mysqldump db - outputs dump of old database ```db```
- | mysql newdb - feeds dump right into new ```newdb``` database on the fly
