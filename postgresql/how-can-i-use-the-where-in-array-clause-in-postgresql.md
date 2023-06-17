# How can I use the WHERE IN array clause in PostgreSQL?
// plain

The WHERE IN array clause can be used in PostgreSQL to compare a set of values against an array of values. It is a shorthand form of multiple OR conditions and can be used to filter a result set.

For example, the following code block will select all rows from the 'users' table where the 'name' column contains any of the values in the array:

```
SELECT name FROM users
WHERE name IN ('John', 'Jane', 'Bob');
```

The output of this code will be a list of all users whose name is either 'John', 'Jane', or 'Bob'.

The code can be broken down into the following parts:

- `SELECT name`: This line specifies which columns to select from the table.
- `FROM users`: This line specifies which table to select from.
- `WHERE name IN ('John', 'Jane', 'Bob')`: This line specifies the criteria to filter the result set. In this case, it will return all rows where the 'name' column contains any of the values in the array.

For more information on the WHERE IN array clause, please refer to the following links:

- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/functions-array.html#ARRAY-COMPARISON-FUNCTIONS-TABLE)
- [W3Schools Tutorial](https://www.w3schools.com/sql/sql_in.asp)

onelinerhub: [How can I use the WHERE IN array clause in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-use-the-where-in-array-clause-in-postgresql)