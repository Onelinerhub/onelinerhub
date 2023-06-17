# How do I use PostgreSQL HStore?
// plain

PostgreSQL HStore is an extension for the PostgreSQL database that allows the storage of key/value data pairs within a single PostgreSQL value. It is commonly used for storing large amounts of data in a single column.

To use PostgreSQL HStore, you must first ensure that the hstore extension is installed and enabled in your database. This can be done with the following command:

```
CREATE EXTENSION hstore;
```

Once the extension is enabled, you can create a table with an hstore column using the following command:

```
CREATE TABLE my_table (
  id serial PRIMARY KEY,
  data hstore
);
```

You can then insert data into the hstore column using the following command:

```
INSERT INTO my_table (data)
VALUES (
  'key1=>value1, key2=>value2'
);
```

You can then query the data from the hstore column using the following command:

```
SELECT * FROM my_table WHERE data->'key1'='value1';
```

You can also use the hstore functions to manipulate the data in the hstore column. For example, the following command will return an array of all the keys in the hstore column:

```
SELECT hstore_keys(data) FROM my_table;
```

## Helpful links

* [PostgreSQL Documentation - HStore](https://www.postgresql.org/docs/current/hstore.html)
* [PostgreSQL Documentation - HStore Functions](https://www.postgresql.org/docs/current/hstore.html#HSTORE-FUNCTIONS)

onelinerhub: [How do I use PostgreSQL HStore?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-hstore)