# Select EXCEPT example

```sql
SELECT col FROM tbl EXCEPT SELECT col FROM tbl1
```

- `col` - column to select from first and second table
- ` tbl ` - first table to select data from
- `tbl1` - second table, to get data from and exclude those rows from result set
- `EXCEPT` - will return results from the left expression but exclude rows from the right expression from final set


