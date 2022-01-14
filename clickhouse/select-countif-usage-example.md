# Select countIf usage example

```sql
SELECT countIf(date > today() - interval 10 day) FROM tbl
```

- `countIf` - count row only if specified expression is `true` 
- `date > today() - interval 10 day` - expression to check (`date` column has date less than 10 days ago)
- `tbl` - table to select data from

group: agregate_if

## Example: 
```sql
SELECT countIf(date > today() - interval 10 day) FROM tbl
```
```
┌─countIf(greater(date, minus(today(), toIntervalDay(10))))─┐
│                                                         6 │
└───────────────────────────────────────────────────────────┘
```

