# Using boolean values

### Clickhouse doesn't support Boolean type, but you can use UInt8 (unsigned 1-byte integer) to implement that:

```sql
CREATE TABLE tbl (date Date, is_ok UInt8) ENGINE = MergeTree ORDER BY date;
INSERT INTO tbl VALUES(today(), 1); -- 1 for true
INSERT INTO tbl VALUES(today(), 0); -- 0 for false
SELECT * FROM tbl WHERE is_ok
```

- `is_ok` - name of the boolean column
- `UInt8` - use unsigned integer to store `1` for true or `0` for false
- `WHERE is_ok` - will filter out rows with `is_ok = 0` (false) and show only rows with `is_ok = 1` (true)


