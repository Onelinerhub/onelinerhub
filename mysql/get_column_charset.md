# Get default charset of a column

```sql
SELECT character_set_name FROM information_schema.columns WHERE table_schema = 'db' AND table_name = 'table' AND column_name = 'column';
```

- character_set_name - will show charset for specified column
- information_schema.columns - system table with meta information for columns of all tables
- 'db' - name of our databse
- 'table' - name of our table
- 'column' - name of our column

group: get_charset
