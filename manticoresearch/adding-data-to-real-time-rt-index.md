# Adding data to real time (RT) index

### Execute this Manticosearch query using [Mysql protocol](/manticoresearch/mysql-client-connection-example):

```sql
INSERT INTO index1 VALUES(1, 'Donald', 'President of UFO')
```

- `INSERT INTO` - inserts data into specified index
- `index1` - name of the [index to insert](/manticoresearch/creating-rt-index) data to
- `1` - document ID
- `'Donald'` - value for [`name` column]((/manticoresearch/creating-rt-index))
- `'President of UFO'` - value for [`description` column](/manticoresearch/creating-rt-index)

group: rt


