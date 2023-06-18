# How do I use foreign keys in SQLite?
// plain

In SQLite, foreign keys are used to link two tables together. A foreign key is a column or a group of columns in a table that points to the primary key of another table.

For example, the following code creates two tables: `customers` and `orders`, and adds a foreign key constraint to `orders` that references `customers`:

```sql
CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  FOREIGN KEY(customer_id) REFERENCES customers(id)
);
```

To insert data into the tables, we can use the following code:

```sql
INSERT INTO customers (name) VALUES ('John Doe');
INSERT INTO orders (customer_id) VALUES (1);
```

The foreign key constraint ensures that the `customer_id` in the `orders` table is a valid `id` from the `customers` table.

## Code explanation

- `CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL)`: This creates the `customers` table with an `id` column as the primary key and a `name` column with a `NOT NULL` constraint.
- `CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(id))`: This creates the `orders` table with an `id` column as the primary key and a `customer_id` column with a `NOT NULL` constraint. The `FOREIGN KEY` clause adds a foreign key constraint to the `orders` table that references the `id` column of the `customers` table.
- `INSERT INTO customers (name) VALUES ('John Doe')`: This inserts a row into the `customers` table with the `name` value of `John Doe`.
- `INSERT INTO orders (customer_id) VALUES (1)`: This inserts a row into the `orders` table with the `customer_id` value of `1`.

## Helpful links
- [SQLite Foreign Key Syntax](https://www.sqlite.org/foreignkeys.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-foreign-key/)

onelinerhub: [How do I use foreign keys in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-foreign-keys-in-sqlite)