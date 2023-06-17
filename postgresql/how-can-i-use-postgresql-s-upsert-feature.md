# How can I use PostgreSQL's UPSERT feature?
// plain

UPSERT is a PostgreSQL feature that allows you to insert or update data in a single operation. It is very useful when you need to insert new records or update existing records in a table.

## Example


```
-- Create a table
CREATE TABLE people (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  age INTEGER
);

-- Insert a new record
INSERT INTO people (name, age)
VALUES ('John', 25);

-- Update the existing record
UPSERT INTO people (id, name, age)
VALUES (1, 'John', 26);
```

## Output example


```
INSERT 0 1
UPSERT 1
```

The code above creates a table called "people" with three columns: id, name, and age. It then inserts a new record with the name "John" and age 25. Lastly, it updates the existing record by using the UPSERT statement. This statement updates the record with id 1, setting the name to "John" and the age to 26.

The syntax for the UPSERT statement is as follows:

```
UPSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

The UPSERT statement can also be used with a WHERE clause to specify which records should be updated or inserted:

```
UPSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...)
WHERE condition;
```

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT).

onelinerhub: [How can I use PostgreSQL's UPSERT feature?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-s-upsert-feature)