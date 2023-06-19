# How can I use Amazon Redshift UNION to combine data from multiple tables?
// plain

Amazon Redshift UNION is a powerful SQL command used to combine data from multiple tables into a single result set. This command can be used to append the data from two tables, or to combine the data from multiple tables into one result set.

## Example code

```
SELECT *
FROM table1
UNION
SELECT *
FROM table2
```

This code will select all columns from both table1 and table2, and combine the data into a single result set. The output of this query will be a table with all the data from both tables.

The code consists of two parts:
1. The first part, `SELECT * FROM table1`, is a SQL query that selects all columns from table1.
2. The second part, `UNION SELECT * FROM table2`, is the UNION command that combines the results of the two queries into one result set.

For more information on using the UNION command in Amazon Redshift, please refer to the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_UNION.html).

onelinerhub: [How can I use Amazon Redshift UNION to combine data from multiple tables?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-redshift-union-to-combine-data-from-multiple-tables)