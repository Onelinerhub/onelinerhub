# Select countIf usage example

```sql
SELECT countIf(date > '2022-01-01') FROM tbl
```

- `countIf` - count row only if specified expression is `true` 
- `date > '2022-01-01'` - expression to check (`date` column has date less than 10 days ago)
- `tbl` - table to select data from

group: agregate_if

## Example: 
```sql
SELECT countIf(date > '2022-01-01') FROM tbl
```
```
┌─countIf(greater(date, '2022-01-01'))─┐
│                                    6 │
└──────────────────────────────────────┘
```

