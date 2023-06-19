# How do I use the NVL function in Amazon Redshift?
// plain

The NVL function in Amazon Redshift is used to replace null values with a specified value. It takes two arguments, the first being the value to be tested for null and the second being the value to be returned if the first argument is null. The syntax is as follows:

```
NVL(value, replacement)
```

For example, if we have a table called `sales` with a column `amount` that contains the following data:

| amount |
| ------ |
| 100    |
| NULL   |
| 300    |

We can use the following query to replace the `NULL` value with `0`:

```
SELECT NVL(amount, 0) AS amount FROM sales;
```

The output of this query would be:

```
amount
100
0
300
```

The parts of the code are:
- `NVL`: The function used to replace null values
- `amount`: The value to be tested for null
- `0`: The value to be returned if `amount` is null
- `SELECT`: The SQL statement used to perform the query
- `AS`: An optional clause used to rename the output column

For more information, please see the following links:
- [NVL Function](https://docs.aws.amazon.com/redshift/latest/dg/r_NVL_function.html)
- [SQL SELECT Statement](https://docs.aws.amazon.com/redshift/latest/dg/r_SELECT_statement.html)

onelinerhub: [How do I use the NVL function in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-nvl-function-in-amazon-redshift)