# Load (import) data into table from a file

```bash
cat file.csv | clickhouse-client -q 'INSERT INTO tbl FORMAT CSV'
```

- file.csv - file with CSV data to import into table
- tbl - name of the table to import data to
- FORMAT CSV - specify CSV format so clickhouse knows how to parse data
