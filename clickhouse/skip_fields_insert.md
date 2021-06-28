# How to skip unknown fields on data insert

```sql
clickhouse-client -n --query="SET input_format_skip_unknown_fields=1; INSERT INTO tbl FORMAT JSONEachRow;"
```

- -n - allow multiple queries
- input_format_skip_unknown_fields=1 - skip unknown fields instead of throwing an error
- tbl - example table to insert data to
- JSONEachRow - example format for data insert
