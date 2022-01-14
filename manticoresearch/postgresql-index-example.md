# Postgresql index example

```bash
source text_src {
  type = pgsql
  sql_host = localhost
  sql_user = usr
  sql_pass = pwd
  sql_db = db
  sql_query = SELECT id, name, description FROM test
}

index text_idx {
  type = plain
  source = text_src
  path = /var/lib/manticore/data/test
}
```

- `text_src` - name of the source block
- `type = pgsql` - we're getting data from Postgresql
- `localhost` - Postgresql host
- `usr` - Postgresql auth username
- `pwd` - Postgresql auth password
- `db` - Postgresql database name
- `sql_query` - query to get data from Postgresql
- `text_idx` - name of the index block and our index
- `/var/lib/manticore/data/test` - path to store index files in

group: index_db


