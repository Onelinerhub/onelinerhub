# Get largest tables list

```sql
SELECT table_name, round(((data_length + index_length) / 1024 / 1024), 2) 'Size, MB'
FROM information_schema.TABLES
ORDER BY data_length + index_length DESC LIMIT 25;
```

- table_name - name of table
- round(((data_length + index_length) / 1024 / 1024), 2) - calculates total table size in MB
- information_schema.TABLES - system table with all tables meta data
- ORDER BY data_length + index_length - show largest tables at the top
- LIMIT 25 - show 25 largest tables (change to your needs)

group: table_sizes
