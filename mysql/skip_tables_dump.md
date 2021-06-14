# Skip certaing tables while doing dump

```bash
mysqldump db --ignore-table=db.table1 --ignore-table=db.table2 > backup.sql
```

- db - database name generate dump for
- --ignore-table= - ignore speicified table while dumping (for multiple tables add this option multiple times)
- db.table1 - first table to ignore
- db.table2 - second table to ignore
- backup.sql - name of dump file

group: dump
