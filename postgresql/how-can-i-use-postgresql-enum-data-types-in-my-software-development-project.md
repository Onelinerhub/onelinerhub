# How can I use PostgreSQL ENUM data types in my software development project?
// plain

PostgreSQL ENUM data types provide a way to define a set of possible values for a column. This can be used to ensure data integrity and avoid errors when inserting data.

## Example code

```
CREATE TYPE status_type AS ENUM ('active', 'inactive', 'deleted');

CREATE TABLE users (
  id serial PRIMARY KEY,
  name varchar(50) NOT NULL,
  status status_type NOT NULL DEFAULT 'active'
);
```

This code creates a `status_type` ENUM type and a `users` table with a `status` column of the `status_type` type. The `status` column will only accept values of `active`, `inactive` and `deleted`.

When inserting data into the `users` table, you can only insert values that are part of the `status_type` ENUM. For example:

```
INSERT INTO users (name, status) VALUES ('John Doe', 'active');
```

This will insert a row with the name `John Doe` and a status of `active`. Attempting to insert a value that is not part of the `status_type` ENUM will result in an error.

## Code explanation

- `CREATE TYPE status_type AS ENUM ('active', 'inactive', 'deleted')`: This creates a `status_type` ENUM type with three possible values: `active`, `inactive`, and `deleted`.
- `CREATE TABLE users (id serial PRIMARY KEY, name varchar(50) NOT NULL, status status_type NOT NULL DEFAULT 'active')`: This creates a `users` table with an `id` column, `name` column, and `status` column of the `status_type` type. The `status` column has a default value of `active`.
- `INSERT INTO users (name, status) VALUES ('John Doe', 'active')`: This inserts a row with the name `John Doe` and a status of `active`.

## Helpful links
- [PostgreSQL Documentation - ENUM Types](https://www.postgresql.org/docs/11/datatype-enum.html)
- [w3resource - PostgreSQL ENUM](https://www.w3resource.com/PostgreSQL/postgresql-enum.php)

onelinerhub: [How can I use PostgreSQL ENUM data types in my software development project?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-enum-data-types-in-my-software-development-project)