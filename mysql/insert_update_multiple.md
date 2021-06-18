# Insert/update multiple rows in single query

```sql
INSERT INTO table (id, col) VALUES (1, 'a'),(2, 'b') ON DUPLICATE KEY UPDATE col = VALUES(col);
```

- INSERT INTO table - standard insert query
- (id, col) - columns list to insert values to (assume ```id``` column is the primary key)
- VALUES (1, 'a'),(2, 'b') - insert 2 rows at once
- ON DUPLICATE KEY UPDATE - update row if we have met duplicate key
- col = VALUES(col) - update ```col``` values if we met duplicate ```id``` for corresponding row

group: insert_update
