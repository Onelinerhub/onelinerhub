# Insert new values only if row doesn't exist already

```sql
INSERT IGNORE INTO table (president_id, name) VALUES(45, 'Donald');
```

- INSERT IGNORE INTO table - this query will cancel insert if the row exists already
- (president_id, name) - columns list to insert values to
- VALUES(45, 'Donald') - values to insert if row doesn't exist (we assume ```president_id``` is primary/unique key)

group: insert_update
