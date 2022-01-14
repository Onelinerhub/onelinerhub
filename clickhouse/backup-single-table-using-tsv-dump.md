# Backup single table using TSV dump

```sql
clickhouse-client -q "SHOW CREATE TABLE tbl FORMAT TabSeparatedRaw" > structure.tsv
clickhouse-client -q "SELECT * FROM tbl FORMAT TSV" | gzip > data.tsv.gz
```

- `clickhouse-client` - CLI client
- `SHOW CREATE TABLE tbl` - will print table creation query
- `structure.tsv` - backup file of a table structure
- `tbl` - table to backup
- `gzip` - will gzip table data for backup
- `data.tsv.gz` - file with table data backup

group: backup


