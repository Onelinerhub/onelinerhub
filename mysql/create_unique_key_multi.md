# Create unique key on multiple columns

```sql
ALTER TABLE table ADD UNIQUE index1(column1, column2, column3);
```

- table - table to add unique index to
- ADD UNIQUE - adds unique key (index)
- index1 - name of unique key
- column1, column2, column3 - list of columns to create unique index on

group: keys
