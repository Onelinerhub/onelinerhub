# How do I configure Elasticsearch to work with PostgreSQL?
// plain

1. First install the PostgreSQL JDBC driver on the Elasticsearch server, as described in the [documentation](https://www.postgresql.org/docs/current/libpq-install.html).

2. Configure the `elasticsearch.yml` file to include the PostgreSQL JDBC driver in the `path.plugins` setting, e.g.

```
path.plugins: /usr/share/elasticsearch/plugins/postgresql-jdbc-driver
```

3. Configure the `elasticsearch.yml` file to include the PostgreSQL connection details, e.g.

```
xpack.sql.jdbc.username: postgres
xpack.sql.jdbc.password: postgres
xpack.sql.jdbc.url: jdbc:postgresql://localhost:5432/postgres
```

4. Restart the Elasticsearch server to apply the changes.

5. Once the server is restarted, run the following command to verify that the PostgreSQL connection is working:

```
curl -XGET 'localhost:9200/_xpack/sql?format=txt'
```

The output should look something like this:

```
{
  "status" : 200,
  "sql" : {
    "jdbc" : {
      "url" : "jdbc:postgresql://localhost:5432/postgres",
      "username" : "postgres"
    }
  }
}
```

6. Once the connection is verified, you can use the `_xpack/sql` endpoint to run SQL queries against the PostgreSQL database.

7. For more information, see the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-access-control.html).

onelinerhub: [How do I configure Elasticsearch to work with PostgreSQL?](https://onelinerhub.com/elasticsearch/how-do-i-configure-elasticsearch-to-work-with-postgresql)