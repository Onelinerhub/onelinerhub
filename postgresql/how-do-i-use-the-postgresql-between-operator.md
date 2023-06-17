# How do I use the PostgreSQL BETWEEN operator?
// plain

The PostgreSQL BETWEEN operator is used to check if a value is within a range of two values. It is inclusive, meaning that the start and end values are included in the range.

The syntax for using the BETWEEN operator is:

```
SELECT <column>
FROM <table>
WHERE <column> BETWEEN <value1> AND <value2>;
```

For example, if you want to retrieve all records from the table 'products' where the price is between $5 and $10, the query would be:

```
SELECT *
FROM products
WHERE price BETWEEN 5 AND 10;
```

The parts of the query are:
- `SELECT *`: Retrieve all columns from the table
- `FROM products`: Specify the table to query
- `WHERE price BETWEEN 5 AND 10`: Filter the records where the price is between $5 and $10

For more information, you can refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/9.1/functions-comparisons.html).

onelinerhub: [How do I use the PostgreSQL BETWEEN operator?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-between-operator)