# How do I create a table in PostgreSQL?
// plain

Creating a table in PostgreSQL is done with the `CREATE TABLE` statement. Here is an example of creating a table called `customers`:

```sql
CREATE TABLE customers (
  customer_id serial PRIMARY KEY,
  customer_name varchar(50) NOT NULL,
  customer_email varchar(255) NOT NULL
);
```

This statement will create a table with three columns:

1. `customer_id`: This column is a serial type and is set as the primary key.
2. `customer_name`: This column is a varchar type with a maximum of 50 characters and is set to not allow null values.
3. `customer_email`: This column is a varchar type with a maximum of 255 characters and is set to not allow null values.

Once the statement is executed, the table will be created and you can begin adding data to it.

## Helpful links

- [PostgreSQL Documentation - CREATE TABLE](https://www.postgresql.org/docs/9.1/sql-createtable.html)
- [PostgreSQL Documentation - Data Types](https://www.postgresql.org/docs/9.1/datatype.html)

onelinerhub: [How do I create a table in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-a-table-in-postgresql)