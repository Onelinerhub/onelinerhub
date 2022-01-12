# Select where date column is between dates

```sql
SELECT * FROM tbl WHERE date BETWEEN '2022-01-11' AND '2022-01-20'
```

- `tbl` - sample table to select data from
- `date` - column of Date type
- `BETWEEN` - filter based on specified values range
- `'2022-01-11'` - start with this value
- `'2022-01-20'` - end with this value

group: where_date

## Example: 
```sql
SELECT * FROM tbl WHERE date BETWEEN '2022-01-11' AND '2022-01-20'
```
```
┌───────date─┬─col────┬─val─┬─age─┐
│ 2022-01-11 │ Donald │   0 │   0 │
│ 2022-01-11 │ Donald │   0 │   0 │
│ 2022-01-12 │ Donald │   0 │   0 │
└────────────┴────────┴─────┴─────┘
```

