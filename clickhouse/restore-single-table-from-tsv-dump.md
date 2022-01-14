# Restore single table from TSV dump

```sql
clickhouse-client < structure.tsv
zcat data.tsv.gz | clickhouse-client -q "INSERT INTO tbl FORMAT TSV"
```

- `clickhouse-client` - CLI client
- `structure.tsv` - table structure file [created during backup](/clickhouse/backup-single-table-using-tsv-dump)
- `data.tsv.gz` - backup file with table data in [gzipped TSV format](/clickhouse/backup-single-table-using-tsv-dump)
- `tbl` - table name to restore
- `INSERT INTO` - will insert given data to `tbl` table

group: backup


