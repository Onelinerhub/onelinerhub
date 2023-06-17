# How do I use a PostgreSQL transaction?
// plain

A PostgreSQL transaction is a sequence of SQL statements that will either all succeed or all fail.

To use a PostgreSQL transaction, you must first begin the transaction with the `BEGIN` command.

```
BEGIN;
```

Then, you can execute any number of SQL statements that you desire. For example:

```
INSERT INTO table1 (col1, col2) VALUES (val1, val2);
UPDATE table2 SET col3 = val3 WHERE col4 = val4;
```

Once all the desired statements have been executed, you must either commit the transaction with the `COMMIT` command or rollback the transaction with the `ROLLBACK` command.

```
COMMIT;
```

If the `COMMIT` command is executed, all the statements within the transaction will be executed. If the `ROLLBACK` command is executed, none of the statements within the transaction will be executed.

## Helpful links

* [PostgreSQL Documentation - Transactions](https://www.postgresql.org/docs/current/transaction-iso.html)
* [PostgreSQL Tutorial - Transactions](https://www.postgresqltutorial.com/postgresql-transaction/)

onelinerhub: [How do I use a PostgreSQL transaction?](https://onelinerhub.com/postgresql/how-do-i-use-a-postgresql-transaction)