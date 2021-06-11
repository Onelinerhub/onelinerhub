# Insert new values or update if row exists

```sql
INSERT INTO table (president_id, name) VALUES(45, 'Donald') ON DUPLICATE KEY UPDATE name = 'Donald T.'
```

- INSERT INTO table - standard insert query
- (president_id, name) - columns list to insert values to
- VALUES(45, 'Donald') - values to insert if row doesn't exist (we assume ```president_id``` is primary/unique key)
- ON DUPLICATE KEY UPDATE - update row if we have met duplicate key
- name = 'Donald T.' - update column ```name``` (we can specify multiple columns comma-separated)
