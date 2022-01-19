# How to create user-defined function

```sql
CREATE FUNCTION test AS (date, age) -> CONCAT(toString(age), ', ', toString(toYear(date)))
```

- `CREATE FUNCTION` - creates specified function
- `test` - name of the function to create (so it can later [be used](/clickhouse/how-to-use-user-defined-function))
- `(date, age)` - arguments list of the function
- `->` - implementation expression goes after this symbol
- `CONCAT(toString(age), ', ', toString(toYear(date)))` - example of extracting a year from `date` argument and concatenating with `age` into final string

group: udf


