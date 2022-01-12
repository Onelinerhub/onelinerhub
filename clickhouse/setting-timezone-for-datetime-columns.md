# Setting timezone for date/time columns

```sql
CREATE TABLE tbl1 (date DateTime('Europe/Lisbon'), col String) ENGINE = MergeTree ORDER BY date;
```

- `tbl1` - name of the table to create
- `DateTime` - set `DateTime` type of `date` column
- `'Europe/Lisbon'` - specify timezone to use for this column as second argument

group: timezone


