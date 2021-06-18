# Disable query caching for specific query

```sql
SELECT SQL_NO_CACHE * FROM table
```

- SQL_NO_CACHE - this will ask mysql to skip caching for current select query
- * FROM table - any standard select query goes here
