# How do I read a SQLite query plan?
// plain

Reading a SQLite query plan is a great way to identify which parts of a query are taking the most time to execute. To read a query plan, use the `EXPLAIN QUERY PLAN` command. This command will return a tree structure that describes the query plan.

Here is an example of the `EXPLAIN QUERY PLAN` command being used on a simple query:

```
sqlite> EXPLAIN QUERY PLAN SELECT * FROM tbl_name;

0|0|0|SEARCH TABLE tbl_name USING INTEGER PRIMARY KEY (rowid=?)
```

The output of the command consists of four parts:
1. The first part is the estimated cost of the query.
2. The second part is the estimated number of rows returned by the query.
3. The third part is the estimated number of columns returned by the query.
4. The fourth part is the query plan itself, which describes the steps that the query will take to execute.

In this example, the query plan is `SEARCH TABLE tbl_name USING INTEGER PRIMARY KEY (rowid=?)`, which means that the query will search the table `tbl_name` using the rowid as the primary key.

For more information on reading query plans, see the [SQLite documentation](https://www.sqlite.org/eqp.html).

onelinerhub: [How do I read a SQLite query plan?](https://onelinerhub.com/sqlite/how-do-i-read-a-sqlite-query-plan)