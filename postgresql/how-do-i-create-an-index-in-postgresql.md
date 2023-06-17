# How do I create an index in PostgreSQL?
// plain

Creating an index in PostgreSQL is quite simple.

1. First, you will need to write an SQL statement that will create the index. For example, to create an index on a column called "id" in a table called "users":
```
CREATE INDEX users_id_idx ON users (id);
```

2. Then, execute the statement using an SQL client or the psql command line tool:
```
psql> CREATE INDEX users_id_idx ON users (id);
CREATE INDEX
```

3. You can check if the index was created by running the \d command:
```
psql> \d users
                               Table "public.users"
   Column   |          Type          | Collation | Nullable | Default
------------+------------------------+-----------+----------+---------
 id         | integer                |           | not null |
...
Indexes:
    "users_id_idx" btree (id)
```

4. The index can be dropped by running the DROP INDEX command:
```
DROP INDEX users_id_idx;
```

5. You can also create a unique index, which ensures that no two rows have the same value in the indexed column:
```
CREATE UNIQUE INDEX users_id_idx ON users (id);
```

6. You can also create an index on multiple columns:
```
CREATE INDEX users_firstname_lastname_idx ON users (first_name, last_name);
```

7. For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/indexes.html).

onelinerhub: [How do I create an index in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-an-index-in-postgresql)