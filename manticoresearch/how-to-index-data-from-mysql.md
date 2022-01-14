# How to index data from Mysql

```txt
source text_src {
  type = mysql
  sql_host = localhost
  sql_user = usr
  sql_pass = pwd
  sql_db = db
  sql_query_pre = SET NAMES utf8
  sql_query = SELECT id, name, description FROM test
}

index text_idx {
  type = plain
  source = text_src
  path = /var/lib/manticore/data/test
}
```

- `text_src` - name of the source block
- `type = mysql` - we're going to index data directly from Mysql
- `localhost` - Mysql host
- `usr` - Mysql auth user
- `pwd` - Mysql auth password
- `db` - Mysql db name
- `sql_query_pre` - query to execute before getting data
- `sql_query` - query to get data for indexing
- `text_idx` - name of the index block and our index
- `/var/lib/manticore/data/test` - path to store index files in


