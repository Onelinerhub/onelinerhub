# Count unique values

```sql
SELECT uniq(col) FROM tbl
```

- `uniq` - will return count of unique values of a given column
- `col` - column to count unique values in
- `tbl` - sample table

group: uniq

## Example: 
```sql
SELECT uniq(col) FROM tbl
```
```
┌─uniq(col)─┐
│         9 │
└───────────┘
```

