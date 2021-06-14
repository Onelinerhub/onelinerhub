# Create dump of a database to a filename with date

```bash
mysqldump db > db-$(date +%Y%m%d).sql
```

- db - database name generate dump for
- db-$(date +%Y%m%d).sql - will generate file names with date (e.g. ```db-20210515.sql```)

group: dump
