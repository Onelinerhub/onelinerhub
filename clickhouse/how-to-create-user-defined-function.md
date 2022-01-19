# How to create user-defined function

```sql
CREATE FUNCTION test AS (date, age) -> CONCAT(toString(age), ', ', toString(toYear(date)))
```


group: udf


