# How to create Buffer table

```sql
CREATE TABLE tbl_buf AS tbl ENGINE = Buffer(default, tbl, 16, 10, 100, 10000, 1000000, 10000000, 100000000);
```

- `tbl_buf` - name of the [Buffer table](https://clickhouse.com/docs/en/engines/table-engines/special/buffer/)
- `AS tbl` - source table to get structure from (we're creating buffer table for `tbl` table)
- `default, tbl` - database name and table name of the source table
- `16` - recommended number of parallel buffers
- `10, 100` - min and max time in seconds to store data to main table from buffer (`tbl` in our case)
- `10000, 1000000` - min and max number of rows to store data to main table from buffer (`tbl` in our case)
- `10000000, 100000000` - min and max size of data (in bytes) to store data to main table from buffer (`tbl` in our case)

group: buffer


link_youtube: https://youtu.be/3np1Co2yW2w
