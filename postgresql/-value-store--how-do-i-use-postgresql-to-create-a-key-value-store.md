# -value store

How do I use PostgreSQL to create a key-value store?
// plain

PostgreSQL can be used to create a key-value store with the help of the hstore extension. To install the extension, you need to run the following code:

```
CREATE EXTENSION hstore;
```

Once the extension is installed, a new data type called `hstore` will be available. This data type allows you to store key-value pairs in a single column. To create a table with an hstore column, you can use the following code:

```
CREATE TABLE my_table (
  id serial PRIMARY KEY,
  data hstore
);
```

You can then insert data into the table using the following code:

```
INSERT INTO my_table (data) VALUES
  ('name => John', 'age => 25', 'city => London');
```

You can then query the data using the `->` operator, which allows you to access the value for a given key. For example:

```
SELECT data->'age' FROM my_table;
```

The output of this query will be `25`.

## Helpful links
- https://www.postgresql.org/docs/9.6/hstore.html
- https://www.postgresqltutorial.com/postgresql-hstore/

onelinerhub: [-value store

How do I use PostgreSQL to create a key-value store?](https://onelinerhub.com/postgresql/-value-store--how-do-i-use-postgresql-to-create-a-key-value-store)