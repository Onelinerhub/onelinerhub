# List all tables from all database

```sql
SELECT database, table FROM system.tables
```

- `system.tables` - system table with info on all databases and tables on the server
- `database, table` - selects database and table name

group: list_db

## Example: 
```sql
SELECT database, table FROM system.tables
```
```
┌─database───────────┬─table──────────────────────────┐
│ INFORMATION_SCHEMA │ COLUMNS                        │
│ INFORMATION_SCHEMA │ SCHEMATA                       │
│ INFORMATION_SCHEMA │ TABLES                         │
│ INFORMATION_SCHEMA │ VIEWS                          │
│ default            │ tbl                            │
│ default            │ tbl1                           │
...
```

