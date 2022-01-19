# Inserting data into table example

### Although Clickhouse allows inserting data row-by-row, **use [bulk insert](/clickhouse/insert-bulk-csv-data-into-table-copy)** to get best performance for large amounts of data.

```sql
INSERT INTO tbl(ts, col) VALUES(now(), 123)
```

- `INSERT INTO` - will insert data into specified table
- `tbl` - name of the table to insert data to
- `ts, col` - column names to specify values for (can be skipped)
- `VALUES` - list of values to insert into row
- `now(), 123` - will insert current datetime into `ts` column and `123` value into `col` column


