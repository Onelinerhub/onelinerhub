# How do I use the PostgreSQL COALESCE function?
// plain

The PostgreSQL `COALESCE` function is used to return the first non-null value from a list of values. It takes in any number of arguments and returns the first one that is not `NULL`.

## Example

```
SELECT COALESCE(NULL, 5, 0);
```
## Output example

```
5
```

The code above will return the value `5` because it is the first non-null value in the list.

The parts of the code are:

- `SELECT`: This is the keyword used to specify that a query is being made.
- `COALESCE`: This is the function being used to return the first non-null value.
- `NULL`: This is a value that is being checked for.
- `5`: This is the value that is returned because it is the first non-null value.
- `0`: This is the last value in the list, but it is not returned because it is not the first non-null value.

For more information on the `COALESCE` function, please see the following link:

[PostgreSQL Documentation](https://www.postgresql.org/docs/9.4/functions-conditional.html#FUNCTIONS-COALESCE-NVL-IFNULL)

onelinerhub: [How do I use the PostgreSQL COALESCE function?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-coalesce-function)