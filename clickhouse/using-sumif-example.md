# Using sumIf example

```sql
SELECT sumIf(age, date < '2022-01-01') FROM tbl
```

- `sumIf` - sum specified column value if expression is `true`
- `age` - name of the column to sum
- `date < '2022-01-01'` - expression to check (should we add this row value to the total sum)
- `tbl` - table to select data from

group: agregate_if


