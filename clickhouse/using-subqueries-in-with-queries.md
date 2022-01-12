# Using subqueries in WITH queries

```sql
WITH (SELECT max(id) FROM tbl) as mxid SELECT * from tbl1 WHERE id > mxid
```

- `WITH` - allows defining user variables
- `SELECT max(id) FROM tbl` - subquery which returns single value
- `mxid` - name of the variable to assign subquery result to
- `id > mxid` - using variable in a query

group: with


