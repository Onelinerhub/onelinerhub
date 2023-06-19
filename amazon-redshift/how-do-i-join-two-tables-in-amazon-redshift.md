# How do I join two tables in Amazon Redshift?
// plain

Joining two tables in Amazon Redshift is a relatively simple process. First, you need to decide which type of join you want to use. The most common join types are inner join, left join, right join, and full outer join.

Once you have decided on the join type, you can use the following SQL statement to join two tables:

```
SELECT *
FROM table1
JOIN table2
ON table1.id = table2.id;
```

This statement will join the two tables on the `id` column. The output of this statement will be a new table containing all of the columns from both tables, with each row representing a join of the two tables.

To further customize the join, you can add additional conditions to the `ON` clause. For example, to join the two tables on the `id` column and the `name` column, you can use the following statement:

```
SELECT *
FROM table1
JOIN table2
ON table1.id = table2.id
AND table1.name = table2.name;
```

You can also use the `USING` clause to specify the columns to join on. For example, to join the two tables on the `id` column, you can use the following statement:

```
SELECT *
FROM table1
JOIN table2
USING (id);
```

For more information about joining tables in Amazon Redshift, please refer to the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_JOIN_clause.html).

onelinerhub: [How do I join two tables in Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-join-two-tables-in-amazon-redshift)