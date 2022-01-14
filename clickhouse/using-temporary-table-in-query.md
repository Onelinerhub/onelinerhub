# Using temporary table in query

```sql
SELECT * FROM tbl WHERE id IN (SELECT id FROM tmp)
```

- `tbl` - standard table to select data from
- `tmp` - name of the [tmp table](/clickhouse/how-to-create-temporary-table) to use in query

group: tmp


## Additional keywords
- tmp

