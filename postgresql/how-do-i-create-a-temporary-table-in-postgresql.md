# How do I create a temporary table in PostgreSQL?
// plain

Creating a temporary table in PostgreSQL is a simple process. Here is an example of how to do it:

```
-- Create a temporary table
CREATE TEMP TABLE items (
  id INTEGER,
  name VARCHAR(50)
);

-- Insert some data
INSERT INTO items (id, name)
VALUES (1, 'Apple'), (2, 'Banana'), (3, 'Orange');

-- Select the data
SELECT * FROM items;

-- Output
id  |  name
----+--------
 1  |  Apple
 2  |  Banana
 3  |  Orange
```

The code above creates a temporary table called `items` with two columns, `id` and `name`. Then it inserts a few rows of data into the table. Finally, it selects the data from the table and prints the output.

The key parts of the code are:

- `CREATE TEMP TABLE` - creates a temporary table
- `INSERT INTO` - inserts data into the table
- `SELECT * FROM` - selects data from the table

For more information, see the PostgreSQL documentation:

- [CREATE TABLE](https://www.postgresql.org/docs/current/sql-createtable.html)
- [INSERT](https://www.postgresql.org/docs/current/sql-insert.html)
- [SELECT](https://www.postgresql.org/docs/current/sql-select.html)

onelinerhub: [How do I create a temporary table in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-a-temporary-table-in-postgresql)