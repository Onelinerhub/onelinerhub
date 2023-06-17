# How do I join two tables in PostgreSQL?
// plain

Joining two tables in PostgreSQL is a common task and can be done with the `JOIN` statement. Here is an example of how to join two tables `table1` and `table2`:

```sql
SELECT *
FROM table1
JOIN table2
ON table1.id = table2.table1_id;
```

The `SELECT` statement is used to select the columns to be returned from the joined tables. The `FROM` clause specifies the tables to be joined, and the `ON` clause specifies the condition for the join. In this example, the `id` column from `table1` is being compared to the `table1_id` column from `table2`.

The output of this query will be a result set containing all columns from both `table1` and `table2`.

The parts of the query are:
- `SELECT`: used to specify the columns to be returned from the joined tables
- `FROM`: used to specify the tables to be joined
- `JOIN`: used to specify the type of join to be performed
- `ON`: used to specify the condition for the join

For more information, see the [PostgreSQL documentation on JOIN](https://www.postgresql.org/docs/current/sql-select.html#SQL-FROM).

onelinerhub: [How do I join two tables in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-join-two-tables-in-postgresql)