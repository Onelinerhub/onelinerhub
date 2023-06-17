# How do I use the PostgreSQL EXPLAIN command?
// plain

The PostgreSQL EXPLAIN command is used to display the execution plan for a query. It shows the steps PostgreSQL will take to execute the query, and the estimated cost of each step.

Here is an example of how to use the EXPLAIN command:

```
EXPLAIN SELECT * FROM customers WHERE city='London';
```

This will return the following output:

```
                                          QUERY PLAN
------------------------------------------------------------------------------------------
Seq Scan on customers  (cost=0.00..1.00 rows=1 width=102)
  Filter: (city = 'London'::text)
(2 rows)
```

This output shows that PostgreSQL will perform a sequential scan on the customers table, and filter the results to only include those with a city of 'London'.

The output includes the estimated cost of the operation (in this case, 0.00..1.00 rows). This cost is an estimate of how much time and resources the query will take to run.

Here is a list of the parts of the output and their meanings:

- Seq Scan: This shows the type of scan PostgreSQL will perform.
- cost: This is the estimated cost of the operation.
- rows: This is the estimated number of rows the query will return.
- width: This is the estimated width of the rows the query will return.

For more information on the EXPLAIN command, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-explain.html).

onelinerhub: [How do I use the PostgreSQL EXPLAIN command?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-explain-command)