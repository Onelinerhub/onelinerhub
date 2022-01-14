# Insert bulk TSV data into table

```sql
cat data.tsv | clickhouse-client -q "INSERT INTO tbl FORMAT TSV"
```

- `data.tsv` - file with TSV data to insert
- `clickhouse-client -q` - execute given query through client interface
- `tbl` - table to insert data into
- `FORMAT TSV` - use `TSV` format for reading data

group: batch_insert


## Additional keywords
- batch

