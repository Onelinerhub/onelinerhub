# Concatenate column values from multiple rows

```sql
SELECT post_id, GROUP_CONCAT(tag SEPARATOR ', ')
FROM post_tags GROUP BY post_id;
```

- SELECT post_id - select id of a post as a first column 
- GROUP_CONCAT(tag SEPARATOR ', ') - will concatenate values from multiple rows based on a grouping rule
- post_tags - our table that has 2 columns: ```post_id, tag```
- GROUP BY post_id - group by ```post_id``` to get concatenated tags list for each post
