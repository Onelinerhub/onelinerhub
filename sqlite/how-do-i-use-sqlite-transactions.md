# How do I use SQLite transactions?
// plain

SQLite transactions are used to ensure data integrity. Transactions are a set of operations that either all succeed or all fail.

To use SQLite transactions, begin a transaction using the `BEGIN TRANSACTION` statement. All subsequent SQL statements will be part of the transaction. When all statements have been executed, use the `COMMIT` statement to save the changes or `ROLLBACK` to undo them.

## Example code

```sql
BEGIN TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

The code above will transfer 100 units from account 1 to account 2. If either of the `UPDATE` statements fail, the `ROLLBACK` statement will undo any changes made.

The code can be broken down as follows:

* `BEGIN TRANSACTION;` - Starts the transaction
* `UPDATE accounts SET balance = balance - 100 WHERE id = 1;` - Subtracts 100 units from account 1
* `UPDATE accounts SET balance = balance + 100 WHERE id = 2;` - Adds 100 units to account 2
* `COMMIT;` - Commits the changes and saves them

For more information, see the [SQLite documentation](https://www.sqlite.org/lang_transaction.html).

onelinerhub: [How do I use SQLite transactions?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-transactions)