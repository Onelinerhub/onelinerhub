# How do I begin a transaction in PostgreSQL?
// plain

To begin a transaction in PostgreSQL, you must use the `BEGIN` command. This command starts a new transaction.

For example, to start a transaction named `my_transaction`:

```
BEGIN TRANSACTION my_transaction;
```

This will start a new transaction and will not make any changes to the database until the transaction is committed.

You can also start a transaction with the `START TRANSACTION` command, which is an alias for `BEGIN`.

```
START TRANSACTION my_transaction;
```

Once a transaction has been started, you can make any changes you want to the database. When you are done making changes, you must commit the transaction using the `COMMIT` command.

```
COMMIT TRANSACTION my_transaction;
```

This will commit any changes you have made in the transaction to the database.

If you decide not to commit the changes, you can rollback the transaction using the `ROLLBACK` command.

```
ROLLBACK TRANSACTION my_transaction;
```

This will undo any changes you have made in the transaction and return the database to its previous state.

## Helpful links
* [PostgreSQL Documentation - BEGIN](https://www.postgresql.org/docs/current/sql-begin.html)
* [PostgreSQL Documentation - COMMIT](https://www.postgresql.org/docs/current/sql-commit.html)
* [PostgreSQL Documentation - ROLLBACK](https://www.postgresql.org/docs/current/sql-rollback.html)

onelinerhub: [How do I begin a transaction in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-begin-a-transaction-in-postgresql)