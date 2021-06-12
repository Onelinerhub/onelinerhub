# Get default charset of a table

```sql
SELECT TABLE_COLLATION FROM information_schema.tables  WHERE table_name = 'table' AND table_schema = 'db';
```

- TABLE_COLLATION - will show default collation for specified table
- information_schema.tables - system table with meta information for tables
- 'table' - name of our table
- 'db' - name of our databse

group: get_charset
