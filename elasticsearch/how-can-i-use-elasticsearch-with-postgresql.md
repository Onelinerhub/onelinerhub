# How can I use Elasticsearch with PostgreSQL?
// plain

Elasticsearch can be used with PostgreSQL by creating a foreign data wrapper (FDW). A FDW is a PostgreSQL extension that allows for connecting to other data sources and querying them as if they were part of the PostgreSQL database.

This can be done by using the `CREATE FOREIGN TABLE` command, which creates a table in PostgreSQL that is actually a link to a table in Elasticsearch.

## Example code

```
CREATE SERVER elasticsearch_server FOREIGN DATA WRAPPER elastic_fdw OPTIONS (host 'localhost', port '9200');

CREATE USER MAPPING FOR postgres SERVER elasticsearch_server OPTIONS (username 'elastic', password 'mypassword');

CREATE FOREIGN TABLE my_table (
  id int,
  name text
) SERVER elasticsearch_server OPTIONS (index 'my_index', type 'my_type');
```

This code creates a server connection to Elasticsearch, a user mapping for PostgreSQL, and a foreign table that is linked to the Elasticsearch index and type.

Once the foreign table is created, it can be queried like any other table in PostgreSQL. For example, to get all documents in the foreign table:

```
SELECT * FROM my_table;
```

## Output example

```
 id | name
----+------
  1 | John
  2 | Jane
  3 | Joe
```

## Code explanation

1. `CREATE SERVER` - creates a server connection to Elasticsearch
2. `CREATE USER MAPPING` - creates a user mapping for PostgreSQL
3. `CREATE FOREIGN TABLE` - creates a foreign table that is linked to the Elasticsearch index and type
4. `SELECT * FROM my_table` - queries the foreign table

## Helpful links
- [Foreign Data Wrappers](https://www.postgresql.org/docs/current/ddl-foreign-data.html)
- [Elasticsearch Foreign Data Wrapper](https://github.com/EnterpriseDB/elastic_fdw)

onelinerhub: [How can I use Elasticsearch with PostgreSQL?](https://onelinerhub.com/elasticsearch/how-can-i-use-elasticsearch-with-postgresql)