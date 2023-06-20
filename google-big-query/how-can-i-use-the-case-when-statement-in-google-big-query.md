# How can I use the CASE WHEN statement in Google Big Query?
// plain

The CASE WHEN statement in Google Big Query is a powerful tool for creating conditional statements in SQL. It allows you to evaluate a set of expressions and return a result based on the evaluation.

For example, the following code block can be used to create a new column in Big Query that returns a string value based on the value of another column:
```
SELECT
  CASE
    WHEN column1 < 0 THEN 'Negative'
    WHEN column1 = 0 THEN 'Zero'
    ELSE 'Positive'
  END AS new_column
FROM my_table
```
The output of this code will be a new column in the table called `new_column` which will contain the string value `Negative`, `Zero`, or `Positive` depending on the value of `column1`.

The syntax of the CASE WHEN statement is as follows:

```
CASE
  WHEN expression1 THEN result1
  WHEN expression2 THEN result2
  ...
  ELSE resultN
END
```

The `expression` can be any valid Big Query expression, such as a comparison expression, a function, etc. The `result` can be any valid Big Query expression, such as a string, an integer, a column, etc.

For more information on the CASE WHEN statement in Big Query, please refer to the [official documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/conditional_functions).

onelinerhub: [How can I use the CASE WHEN statement in Google Big Query?](https://onelinerhub.com/google-big-query/how-can-i-use-the-case-when-statement-in-google-big-query)