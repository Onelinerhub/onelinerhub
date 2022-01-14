# Setting primary key for a table

```sql
CREATE TABLE tbl (event String, ts DateTime) ENGINE = MergeTree PARTITION BY toDate(ts) ORDER BY (event, ts)
```

- `tbl` - name of the table to create (and set primary key)
- `ORDER BY` - sorting order will also be used as primary key
- `(event, ts)` - primary key (and table sorting order) columns


