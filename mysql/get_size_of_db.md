# Get total size of specific databse

```sql
SELECT ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) FROM information_schema.tables WHERE table_schema = 'db';
```

- ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) - will return final size in Megabytes
- information_schema.tables - system table with meta data for all tables on server
- table_schema = 'db' - we get total size for ```db``` database

group: table_sizes
