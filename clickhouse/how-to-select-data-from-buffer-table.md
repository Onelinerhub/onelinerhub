# How to select data from Buffer table

### Not that selecting data from Buffer table will automatically merge results from Buffer and source tables for you. So if you have Buffer tables created you should **always** select data from it (and not from source table):

```sql
SELECT count(*) FROM tbl_buf
```

- `tbl_buf` - name of the [Buffer table](https://clickhouse.com/docs/en/engines/table-engines/special/buffer/) to select data from
- `SELECT count(*) FROM` - sample select query

group: buffer


