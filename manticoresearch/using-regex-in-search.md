# Using regex in search

### Execute this Manticosearch query using [Mysql protocol](/manticoresearch/mysql-client-connection-example):

```sql
SELECT * FROM index1 WHERE REGEX(name, 'D.+');
```

- `SELECT * FROM` - search data in specified index
- `index1` - name of the index to search in
- `WHERE` - list search conditions
- `REGEX` - function to match regex to the specified attribute
- `name` - name of the attribute to match against regular expression
- `'D.+'` - regular expression pattern to check


