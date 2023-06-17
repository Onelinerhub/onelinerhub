# How do I create a foreign key in PostgreSQL?
// plain

Creating a foreign key in PostgreSQL is a simple process. First, create a table with the necessary columns and data types. For example:

```
CREATE TABLE parent_table (
   id SERIAL PRIMARY KEY,
   name VARCHAR(50) NOT NULL
);
```

Then, create a second table with a foreign key column that references the primary key from the first table.

```
CREATE TABLE child_table (
   id SERIAL PRIMARY KEY,
   parent_id INTEGER REFERENCES parent_table(id)
);
```

The `REFERENCES` clause in the above statement creates a foreign key constraint. This constraint ensures that the value of the `parent_id` column in the `child_table` must match the value of the `id` column in the `parent_table`.

You can also add additional constraints, such as `ON DELETE CASCADE`, to the foreign key. This will ensure that when a row in the parent table is deleted, all corresponding rows in the child table are also deleted.

```
CREATE TABLE child_table (
   id SERIAL PRIMARY KEY,
   parent_id INTEGER REFERENCES parent_table(id) ON DELETE CASCADE
);
```

For more information on creating foreign key constraints in PostgreSQL, see the official documentation: [https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK)

onelinerhub: [How do I create a foreign key in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-a-foreign-key-in-postgresql)