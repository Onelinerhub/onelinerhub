# How to use user-defined function

```sql
SELECT test(date, age) FROM tbl
```

- `test(` - name of the [created user-defined function](/clickhouse/how-to-create-user-defined-function)
- `date, age` - arguments of the user-defined function (in our case - `date` and `age` columns)
- `tbl` - table to select data from

group: udf

## Example: 
```sql
SELECT test(date, age) FROM tbl LIMIT 5
```
```
┌─concat(toString(age), ', ', toString(toYear(date)))─┐
│ 0, 1970                                             │
│ 125, 1970                                           │
│ 0, 1970                                             │
│ 125, 1970                                           │
│ 0, 1970                                             │
└─────────────────────────────────────────────────────┘
```

