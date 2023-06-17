# How do I use PostgreSQL data types?
// plain

PostgreSQL data types are used to specify the kind of data that a column can hold in a table. To use PostgreSQL data types, you must first create a table and specify the columns and their data types. For example, the following code creates a table called 'users' with two columns, 'name' and 'age', and assigns the data type 'varchar' to the 'name' column and 'integer' to the 'age' column:

```
CREATE TABLE users (
    name varchar,
    age integer
);
```

This code creates a table called 'users' with two columns, 'name' and 'age', and assigns the data type 'varchar' to the 'name' column and 'integer' to the 'age' column.

1. `CREATE TABLE users` - creates a table called `users`
2. `(name varchar, age integer)` - defines two columns called `name` and `age` and assigns the data types `varchar` and `integer` to them respectively

PostgreSQL data types are used to ensure that the data stored in a column is of the correct type. For example, if a column is defined as an `integer`, then only integer values can be stored in that column.

## Helpful links

- [PostgreSQL Documentation - Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [PostgreSQL Tutorial - Create Table](https://www.postgresqltutorial.com/postgresql-create-table/)

onelinerhub: [How do I use PostgreSQL data types?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-data-types)