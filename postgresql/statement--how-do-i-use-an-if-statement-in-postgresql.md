# statement

How do I use an IF statement in PostgreSQL?
// plain

An IF statement in PostgreSQL is a conditional statement that allows you to execute a set of SQL commands depending on a certain condition. It is similar to an IF statement in other programming languages.

The syntax for an IF statement in PostgreSQL is as follows:

```
IF condition THEN
   statements;
END IF;
```

The `condition` is a boolean expression that evaluates to `TRUE` or `FALSE`. If the condition evaluates to `TRUE`, the statements within the `THEN` clause are executed.

For example, the following code block will check if the value of the `grade` column is greater than or equal to 4. If it is, it will set the `passed` column to `TRUE`:

```
IF grade >= 4 THEN
   UPDATE students SET passed = TRUE;
END IF;
```

The parts of the IF statement are:
* `IF`: This is the keyword that begins the statement.
* `condition`: This is a boolean expression that evaluates to `TRUE` or `FALSE`.
* `THEN`: This is the keyword that separates the condition from the statements to be executed.
* `statements`: This is a set of SQL commands to be executed if the condition evaluates to `TRUE`.
* `END IF`: This is the keyword that ends the statement.

For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-if.html).

onelinerhub: [statement

How do I use an IF statement in PostgreSQL?](https://onelinerhub.com/postgresql/statement--how-do-i-use-an-if-statement-in-postgresql)