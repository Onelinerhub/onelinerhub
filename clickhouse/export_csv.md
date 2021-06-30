# Export table to CSV file

```bash
clickhouse-client --query "SELECT * from tbl" --format CSV > file.csv
```

- tbl - name of the table to export data from
- --format CSV - specify CSV format for export
- file.csv - file to save CSV data to

group: import_export
