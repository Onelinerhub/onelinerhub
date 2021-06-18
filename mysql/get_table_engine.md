# Get table engine

```sql
SELECT engine FROM information_schema.tables WHERE table_name = 'table' AND table_schema = 'db';
```

- engine - will return specified table engine
- information_schema.tables - system table with metadata
- 'table' - table name to get engine for
- 'db' - database name where table is located
