# How do I use PostgreSQL's MERGE statement?
// plain

The PostgreSQL MERGE statement is a powerful way to combine data from multiple sources into a single table. It allows you to efficiently update, insert, and delete data in a table based on data from other tables.

Here is an example of how to use the MERGE statement:

```
MERGE INTO target_table USING source_table
ON (target_table.id = source_table.id)
WHEN MATCHED THEN
  UPDATE SET target_table.value = source_table.value
WHEN NOT MATCHED THEN
  INSERT (id, value) VALUES (source_table.id, source_table.value);
```

This example code will update the `target_table` with any matching rows from the `source_table`, and insert any new rows from the `source_table` into the `target_table`.

The code can be broken down into the following parts:

* `MERGE INTO` is used to specify the target table for the operation.
* `USING` is used to specify the source table for the operation.
* `ON` is used to specify the join condition between the target and source tables.
* `WHEN MATCHED THEN` is used to specify the action to take on rows that match the join condition.
* `WHEN NOT MATCHED THEN` is used to specify the action to take on rows that do not match the join condition.

For more information about the PostgreSQL MERGE statement, please see the following links:

* [PostgreSQL Documentation: MERGE](https://www.postgresql.org/docs/current/sql-merge.html)
* [PostgreSQL Tutorial: MERGE](https://www.postgresqltutorial.com/postgresql-merge/)

onelinerhub: [How do I use PostgreSQL's MERGE statement?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-merge-statement)