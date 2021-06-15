# Export database tables structure without data

```sql
mysqldump --no-data db > structure.sql
```

- --no-data - will dump only tables structures
- db - name of database to export structure for
- structure.sql - file to save tables structure to
