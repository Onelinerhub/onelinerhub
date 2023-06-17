# How do I use PostgreSQL's bigserial data type?
// plain

PostgreSQL's `bigserial` data type is an auto-incrementing 64-bit integer. It is used to generate a unique number for each row in a table. This can be useful when a unique identifier is needed for each record in a table, such as a primary key.

## Example code

```
CREATE TABLE users (
    id bigserial PRIMARY KEY,
    name varchar(255) NOT NULL
);
```

This code creates a table with a `bigserial` column named `id` that is set as the primary key. After creating the table, you can insert records into it and `id` will automatically be assigned a unique number.

## Code explanation


1. `CREATE TABLE`: This is a SQL command used to create a new table.
2. `id bigserial PRIMARY KEY`: This creates a `bigserial` column named `id` and sets it as the primary key.
3. `name varchar(255) NOT NULL`: This creates a `varchar` column named `name` that is not allowed to be `NULL`.

## Helpful links

- [PostgreSQL Documentation - bigserial](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-SERIAL)
- [W3Schools - SQL CREATE TABLE](https://www.w3schools.com/sql/sql_create_table.asp)

onelinerhub: [How do I use PostgreSQL's bigserial data type?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-bigserial-data-type)