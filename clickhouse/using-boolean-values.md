# Using boolean values

### Clickhouse doesn't support Boolean type, but you can use UInt8 (unsigned 1-byte integer) to implement that:

```sql
CREATE TABLE tbl (date Date, is_ok UInt8) ENGINE = MergeTree ORDER BY date;
INSERT INTO tbl VALUES(today(), 1); -- 1 for true
INSERT INTO tbl VALUES(today(), 0); -- 0 for false
```



