# Searching data in real time (RT) index using SQL

### Execute this Manticosearch query using [Mysql protocol](/manticoresearch/mysql-client-connection-example):

```sql
SELECT * FROM index1 WHERE match('other')
```

- `SELECT * FROM` - search data in specified index
- `index1` - name of the [index to search](/manticoresearch/creating-rt-index) data in
- `WHERE` - list search conditions
- `match` - execute full text search based on specified search phrase
- `other` - phrase to search for in index

group: rt


