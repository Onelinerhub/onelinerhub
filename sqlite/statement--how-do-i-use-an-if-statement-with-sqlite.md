# statement

How do I use an if statement with SQLite?
// plain

An if statement can be used with SQLite to execute code based on a condition. The syntax for using an if statement is as follows:

```
IF condition
    THEN statement
END IF;
```

The `condition` is an expression that evaluates to either true or false. The `statement` is a SQL statement that is executed if the condition is true.

For example, the following code will print "Condition is true" if the value of `x` is greater than 0:

```
DECLARE x INT;
SET x = 5;

IF x > 0
    THEN SELECT 'Condition is true';
END IF;
```

## Output example

```
Condition is true
```

The code consists of the following parts:

- `DECLARE x INT;`: Declares the variable `x` as an integer.
- `SET x = 5;`: Sets the value of `x` to 5.
- `IF x > 0`: Evaluates the condition to check if the value of `x` is greater than 0.
- `THEN SELECT 'Condition is true';`: Executes the `SELECT` statement if the condition is true.
- `END IF;`: Closes the `IF` statement.

For more information, see the [SQLite IF documentation](https://www.sqlite.org/lang_expr.html#if).

onelinerhub: [statement

How do I use an if statement with SQLite?](https://onelinerhub.com/sqlite/statement--how-do-i-use-an-if-statement-with-sqlite)