# Output totals together with resulting table

```sql
SELECT count(*), date FROM tbl GROUP BY date WITH TOTALS;
```

- `count(*), date` - what to select 
- `tbl` - table to get data from
- `GROUP BY date` - group data by `date` column
- `WITH TOTALS` - will add additional row to the result set with summary data 

group: summary

## Example: 
```sql
SELECT count(*), date FROM tbl GROUP BY date WITH TOTALS;
```
```
┌─count()─┬───────date─┐
│       1 │ 2022-01-07 │
│       1 │ 2022-01-10 │
│       2 │ 2022-01-11 │
│       1 │ 2022-01-12 │
└─────────┴────────────┘

Totals:
┌─count()─┬───────date─┐
│       5 │ 1970-01-01 │
└─────────┴────────────┘
```

