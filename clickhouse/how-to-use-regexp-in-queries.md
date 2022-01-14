# How to use regex in queries

```sql
SELECT * FROM tbl WHERE match(col, 'D.+')
```

- `tbl` - table to select data from based on regex
- `match` - match given pattern against column
- `col` - name of the column to check regular expression on
- `'D.+'` - regex pattern to use (find all values starting with `D` in our case)


