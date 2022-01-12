# Select with datetime column values

```sql
SELECT * FROM tbl WHERE dt > toDateTime('2030-01-01 01:02:03')
```

- `dt` - column of DateTime type
- `toDateTime` - converts given string to DateTime
- `'2030-01-01 01:02:03'` - sample date/time to use in query

group: where_date


