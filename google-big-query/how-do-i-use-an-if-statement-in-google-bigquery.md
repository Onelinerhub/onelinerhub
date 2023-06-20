# How do I use an IF statement in Google BigQuery?
// plain

An IF statement in Google BigQuery is used to create a conditional statement that returns a value or performs an action based on a condition. It is used to test a condition and execute a statement accordingly.

```
SELECT IF(expr1, expr2, expr3)
```

This is the syntax for an IF statement in BigQuery. `expr1` is a boolean expression that is evaluated to determine if the statement should be executed. `expr2` is the value that is returned if the expression evaluates to true. `expr3` is the value that is returned if the expression evaluates to false.

For example, the following query will return the value `'Yes'` if the `age` column is greater than 18 and `'No'` otherwise:

```
SELECT IF(age > 18, 'Yes', 'No')
```

The parts of the IF statement are:
- `IF`: This is the keyword used to start the IF statement.
- `expr1`: This is a boolean expression that is evaluated to determine if the statement should be executed.
- `expr2`: This is the value that is returned if the expression evaluates to true.
- `expr3`: This is the value that is returned if the expression evaluates to false.

## Helpful links
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#if_operator)

onelinerhub: [How do I use an IF statement in Google BigQuery?](https://onelinerhub.com/google-big-query/how-do-i-use-an-if-statement-in-google-bigquery)