# Using multiIf in query

```sql
SELECT multiIf(date < '2022-01-01', 'last_year', date = today(), 'today', 'recent') FROM tbl
```

- `multiIf` - returns multiple variants based on multiple conditions
- `date < '2022-01-01'` - first condition to check
- `'last_year'` - return this value if first condition is `true`
- `date = today()` - second condition to check
- `'today'` - return this value if second condition is `true`
- `'recent'` - return last value is all other conditions are `false`
- `tbl` - table to select data from

group: agregate_if

## Example: 
```sql
SELECT multiIf(date < '2022-01-01', 'last_year', date = today(), 'today', 'recent') FROM tbl
```
```
┌─human_date─┐
│ last_year  │
│ last_year  │
│ recent     │
│ recent     │
│ recent     │
│ recent     │
│ recent     │
│ recent     │
└────────────┘
```

