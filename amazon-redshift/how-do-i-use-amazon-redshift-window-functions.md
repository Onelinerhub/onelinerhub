# How do I use Amazon Redshift window functions?
// plain

Amazon Redshift window functions provide a way to perform calculations across a set of rows that are related to the current row. This is done by using an OVER clause to define the set of rows used for the calculation.

## Example


```
SELECT
  id,
  avg(value) OVER (PARTITION BY id)
FROM table;
```

This example will calculate the average value for each id. The `PARTITION BY` clause defines the set of rows used for the calculation.

Parts of the code:
- `SELECT`: This clause is used to specify the columns to be returned by the query.
- `id`: This is the column that will be used to partition the data for the calculation.
- `avg(value)`: This is the function used to calculate the average value.
- `OVER`: This clause defines the set of rows used for the calculation.
- `PARTITION BY id`: This clause specifies the column used to partition the data.

## Helpful links
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/c_window_functions.html)
- [Postgres Documentation](https://www.postgresql.org/docs/9.4/tutorial-window.html)

onelinerhub: [How do I use Amazon Redshift window functions?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-window-functions)