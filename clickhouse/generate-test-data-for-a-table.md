# Generate test data for a table

```sql
INSERT INTO tbl(date, val) SELECT today(), number FROM numbers(10000)
```

- `tbl` - table to insert generated data to
- `date, val` - columns to fill with generated data
- `today()` - set today value for `date` column
- `number` - set `number` value for `col` column
- `numbers(10000)` - will generate 10k rows with `number` column value in a 1...10000 range


