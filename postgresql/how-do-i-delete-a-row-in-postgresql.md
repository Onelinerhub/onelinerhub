# How do I delete a row in PostgreSQL?
// plain

To delete a row in PostgreSQL, the `DELETE` statement is used. The `DELETE` statement requires the `WHERE` clause to identify the row to be deleted.

For example, the following statement deletes a row from the `customers` table with `customer_id` equal to `5`:
```
DELETE FROM customers
WHERE customer_id = 5;
```

No output will be produced after executing the statement.

The parts of the code are as follows:
- `DELETE`: the keyword used for deleting a row
- `FROM customers`: the table from which the row is deleted
- `WHERE customer_id = 5`: the condition used to identify the row to be deleted

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [DELETE Statement](https://www.postgresql.org/docs/current/sql-delete.html)

onelinerhub: [How do I delete a row in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-delete-a-row-in-postgresql)