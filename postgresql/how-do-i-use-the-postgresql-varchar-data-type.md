# How do I use the PostgreSQL VARCHAR data type?
// plain

The PostgreSQL `VARCHAR` data type is used to store character strings of variable length. It is similar to `CHAR` except that it stores strings of variable length up to a maximum of `n` characters, where `n` is the specified length of the column.

For example, to create a `VARCHAR` column with a maximum length of 10 characters:

```sql
CREATE TABLE products (
    product_name VARCHAR(10)
);
```

The parts of this code are:

- `CREATE TABLE`: the SQL command used to create a new table
- `products`: the name of the new table
- `product_name`: the name of the column
- `VARCHAR(10)`: the data type and maximum length of the column

When inserting data into the `product_name` column, the value must not exceed 10 characters.

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/datatype-character.html).

onelinerhub: [How do I use the PostgreSQL VARCHAR data type?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-varchar-data-type)