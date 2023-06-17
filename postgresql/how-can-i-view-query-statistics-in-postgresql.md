# How can I view query statistics in PostgreSQL?
// plain

To view query statistics in PostgreSQL, you can use the `EXPLAIN` command. This command will show you the execution plan for a given query. This plan will include information about the cost of each operation in the query, as well as the estimated number of rows that will be returned.

For example, the following query will show the execution plan for a SELECT statement:

```
EXPLAIN SELECT * FROM mytable;
```

The output of this command might look like this:

```
                                          QUERY PLAN
------------------------------------------------------------------------------------------------
 Seq Scan on mytable  (cost=0.00..2.00 rows=100 width=20)
(1 row)
```

The output shows that the query will do a sequential scan of the table, with a cost of 2 and an estimated number of rows of 100.

You can also use the `ANALYZE` command to get more detailed query statistics. This command will run the query and collect statistics about the query execution.

For example, the following query will analyze a SELECT statement:

```
ANALYZE SELECT * FROM mytable;
```

The output of this command might look like this:

```
                                          QUERY PLAN
------------------------------------------------------------------------------------------------
 Seq Scan on mytable  (cost=0.00..2.00 rows=100 width=20)
(1 row)

Time: 0.002s
```

The output shows the same query plan as before, but also includes the time it took to execute the query (in this case, 0.002s).

You can find more information about the `EXPLAIN` and `ANALYZE` commands in the [PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-explain.html).

onelinerhub: [How can I view query statistics in PostgreSQL?](https://onelinerhub.com/postgresql/how-can-i-view-query-statistics-in-postgresql)