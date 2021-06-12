# Concatenate column values from multiple rows

```sql
SET GLOBAL sql_mode = (SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''));
```

- GLOBAL sql_mode - will update configuration parameter for the whole server
- @@sql_mode - will fetch the same variable current value
- 'ONLY_FULL_GROUP_BY', '' - will remove ```ONLY_FULL_GROUP_BY``` from ```sql_mode``` variable
