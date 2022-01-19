# How to execute SQL query from a file

```sql
clickhouse-client < /tmp/test.sql
```

- `clickhouse-client` - CLI client
- `/tmp/test.sql` - path to the file with SQL queries

## Example: 
```sql
echo 'SELECT NOW()' > /tmp/test.sql;
clickhouse-client < /tmp/test.sql;
```
```
2022-01-19 14:26:38
```

