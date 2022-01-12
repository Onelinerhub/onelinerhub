# Using multiple variables in "WITH" queries

```sql
WITH 1 AS a, 100 as b SELECT * FROM tbl WHERE col > a AND col < b
```

- `WITH` - allows defining user variables
- `1 AS a` - first variable and value
- `100 as b` - second variable and value
- `col > a AND col < b` - using both variable in a query

group: with


