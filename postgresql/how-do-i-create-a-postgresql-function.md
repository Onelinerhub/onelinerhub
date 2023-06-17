# How do I create a PostgreSQL function?
// plain

Creating a PostgreSQL function is simple and straightforward. To create a function, you must use the `CREATE FUNCTION` statement. The syntax is as follows:

```sql
CREATE FUNCTION function_name(parameter_list)
RETURNS return_type AS
$$
BEGIN
    -- function body
END;
$$
LANGUAGE language_name;
```

The `function_name` is the name of the function to be created. The `parameter_list` is a comma-separated list of parameters that the function will accept. The `return_type` is the data type of the value that the function will return. The `language_name` is the programming language used to write the function body.

For example, the following function takes two parameters, `a` and `b`, and returns the sum of the two parameters:

```sql
CREATE FUNCTION add_two_numbers(a INT, b INT)
RETURNS INT AS
$$
BEGIN
    RETURN a + b;
END;
$$
LANGUAGE plpgsql;
```

The output of the above code is:

```
CREATE FUNCTION
```

### List of code parts explanation

1. `CREATE FUNCTION`: This is the statement used to create a PostgreSQL function.
2. `function_name`: This is the name of the function to be created.
3. `parameter_list`: This is a comma-separated list of parameters that the function will accept.
4. `return_type`: This is the data type of the value that the function will return.
5. `language_name`: This is the programming language used to write the function body.
6. `RETURN`: This statement is used to return a value from the function.

### Relevant Links

1. [PostgreSQL Documentation - CREATE FUNCTION](https://www.postgresql.org/docs/current/sql-createfunction.html)
2. [PostgreSQL Documentation - Language Support](https://www.postgresql.org/docs/current/sql-createfunction.html#SQL-CREATEFUNCTION-LANGUAGE)

onelinerhub: [How do I create a PostgreSQL function?](https://onelinerhub.com/postgresql/how-do-i-create-a-postgresql-function)