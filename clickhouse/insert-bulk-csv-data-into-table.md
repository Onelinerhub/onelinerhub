# Insert bulk CSV data into table

```sql
cat data.csv | clickhouse-client -q "INSERT INTO tbl FORMAT CSV"
```

- `data.csv` - file with CSV data to insert
- `clickhouse-client -q` - execute given query through client interface
- `tbl` - table to insert data into
- `FORMAT CSV` - use `CSV` format for reading data

group: batch_insert


## Additional keywords
- batch

