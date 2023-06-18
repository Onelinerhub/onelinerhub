# How do I begin a transaction in SQLite?
// plain

To begin a transaction in SQLite, you must use the `BEGIN TRANSACTION` command. This command will start a new transaction and will allow you to execute a series of SQL commands as a single unit.

For example, the following code will start a new transaction and insert two records into the `users` table:

```sql
BEGIN TRANSACTION;
INSERT INTO users (name, age) VALUES ('John', 25);
INSERT INTO users (name, age) VALUES ('Jane', 30);
COMMIT;
```

This code will execute without any output.

The code consists of the following parts:
- `BEGIN TRANSACTION;` - This starts a new transaction.
- `INSERT INTO users (name, age) VALUES ('John', 25);` - This inserts a new record into the `users` table.
- `INSERT INTO users (name, age) VALUES ('Jane', 30);` - This inserts a second record into the `users` table.
- `COMMIT;` - This commits the changes and ends the transaction.

For more information, please refer to the [SQLite documentation](https://www.sqlite.org/lang_transaction.html).

onelinerhub: [How do I begin a transaction in SQLite?](https://onelinerhub.com/sqlite/how-do-i-begin-a-transaction-in-sqlite)