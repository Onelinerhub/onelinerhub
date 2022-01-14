# Insert bulk data into table

```sql
INSERT INTO tbl(date, col) VALUES(today(), 'hi'),(today(), 'good'),...
```

- `tbl` - table to insert bulk data into
- `date, col` - columns to insert data to
- `VALUES` - values list (insert as much rows as you like)
- `(today(), 'hi')` - first row of data to insert
- `(today(), 'good')` - second row of data to insert
- `...` - additional (any number of rows) data to insert

group: batch_insert


