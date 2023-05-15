# How to use variables in Mariadb?
// plain

Variables in MariaDB are used to store values for use in SQL statements. Variables can be declared and assigned values using the `SET` statement.

## Example

```
SET @myvar = 10;
```

This statement declares a variable `@myvar` and assigns it the value `10`.

The parts of the code are:
- `SET`: the keyword used to declare and assign values to variables
- `@myvar`: the name of the variable
- `=`: the operator used to assign a value to a variable
- `10`: the value assigned to the variable

Variables can be used in SQL statements in place of literal values. For example:

```
SELECT * FROM mytable WHERE mycolumn = @myvar;
```

This statement will select all rows from the table `mytable` where the column `mycolumn` has the value `10`.

## Helpful links
- [MariaDB Documentation - User-Defined Variables](https://mariadb.com/kb/en/library/user-defined-variables/)

onelinerhub: [How to use variables in Mariadb?](https://onelinerhub.com/mariadb/how-to-use-variables-in-mariadb)