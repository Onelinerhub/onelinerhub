# How to use XA transactions in Mariadb?
// plain

XA transactions are distributed transactions that allow multiple databases to be involved in a single transaction. In MariaDB, XA transactions are supported through the XA START, XA END, XA PREPARE, XA COMMIT, and XA ROLLBACK commands.

## Example

```
XA START 'xid1'
INSERT INTO table1 VALUES (1,2,3);
XA END 'xid1';
XA PREPARE 'xid1';
XA COMMIT 'xid1';
```

The above example starts an XA transaction with the XA START command, inserts a row into a table with the INSERT command, ends the transaction with the XA END command, prepares the transaction with the XA PREPARE command, and commits the transaction with the XA COMMIT command.

## Code explanation


1. XA START 'xid1': This command starts an XA transaction with the given transaction identifier (xid1).
2. INSERT INTO table1 VALUES (1,2,3): This command inserts a row into the table1 table with the given values.
3. XA END 'xid1': This command ends the XA transaction with the given transaction identifier (xid1).
4. XA PREPARE 'xid1': This command prepares the XA transaction with the given transaction identifier (xid1).
5. XA COMMIT 'xid1': This command commits the XA transaction with the given transaction identifier (xid1).

## Helpful links

- [MariaDB Documentation - XA Transactions](https://mariadb.com/kb/en/library/xa-transactions/)

onelinerhub: [How to use XA transactions in Mariadb?](https://onelinerhub.com/mariadb/how-to-use-xa-transactions-in-mariadb)