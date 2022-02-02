# How to execute SQL query from a file

```bash
clickhouse-client < /tmp/test.sql
```

- `clickhouse-client` - CLI client
- `/tmp/test.sql` - path to the file with SQL queries

## Example: 
```bash
echo 'SELECT NOW()' > /tmp/test.sql;
clickhouse-client < /tmp/test.sql;
```
```
2022-01-19 14:26:38
```

link_youtube: https://youtu.be/1kbZiH9EPHA
