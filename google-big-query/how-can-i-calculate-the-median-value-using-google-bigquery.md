# How can I calculate the median value using Google BigQuery?
// plain

Calculating the median value using Google BigQuery is relatively simple. To calculate the median, you can use the `PERCENTILE_CONT` function. This function takes two arguments, the first being the expression which will be used to calculate the median, and the second being the percentile which is 0.5 to calculate the median.

For example, the following code will calculate the median `salary` value from the `employees` table:

```
SELECT PERCENTILE_CONT(salary, 0.5) AS median_salary
FROM employees;
```

The output of this code will be the median salary of the employees table:

```
median_salary
45000
```

The code consists of the following parts:
1. `SELECT` - This statement specifies the columns or expressions that are returned by the query.
2. `PERCENTILE_CONT` - This function takes two arguments, the first being the expression which will be used to calculate the median, and the second being the percentile which is 0.5 to calculate the median.
3. `AS median_salary` - This statement specifies the column name of the output.

For more information on the `PERCENTILE_CONT` function, please see the [documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#percentile_cont).

onelinerhub: [How can I calculate the median value using Google BigQuery?](https://onelinerhub.com/google-big-query/how-can-i-calculate-the-median-value-using-google-bigquery)