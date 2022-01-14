# Creating real time (RT) index

### Execute this Manticosearch query using [Mysql protocol](/manticoresearch/mysql-client-connection-example):

```sql
CREATE TABLE index1(name text, description text)
```

- `CREATE TABLE` - Creates specified rt index
- `index1` - name of the index to create
- `name` - first field of `text` [type](https://manual.manticoresearch.com/Creating_an_index/Data_types#Data-types)
- `description` - second field of `text` [type](https://manual.manticoresearch.com/Creating_an_index/Data_types#Data-types)

group: rt


