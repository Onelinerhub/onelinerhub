# How to delete data

```sql
ALTER TABLE tbl DELETE WHERE time < now() - 60
```

- tbl - name of the table to delete data from
- WHERE time < now() - 60 - condition to delete data on (```time``` column less than 60 seconds ago, in our case)
