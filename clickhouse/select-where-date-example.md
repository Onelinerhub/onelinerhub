# Select with date column values

```sql
SELECT * FROM tbl WHERE date = toDate('2022-01-12')
```

- `toDate` - converts string to date
- `date` - date column
- `'2022-01-12'` - sample date to use in select

group: where_date

## Example: 
```sql
SELECT * FROM tbl WHERE date = toDate('2022-01-12')
```
```
┌───────date─┬─col────┬─val─┬─age─┐
│ 2022-01-12 │ Donald │   0 │   0 │
└────────────┴────────┴─────┴─────┘
```

