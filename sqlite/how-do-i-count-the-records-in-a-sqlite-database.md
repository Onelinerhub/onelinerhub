# How do I count the records in a SQLite database?
// plain

To count the records in a SQLite database, you can use the `SELECT COUNT` statement. This statement will return the total number of records in the specified table.

For example, to count the records in a table named `customers`, the following code can be used:

```sql
SELECT COUNT(*)
FROM customers;
```

The output of the above code will be the total number of records in the `customers` table.

The code consists of the following parts:
1. `SELECT COUNT(*)` - This part of the code specifies the operation to be performed, which is to count the number of records in the table.
2. `FROM customers` - This part of the code specifies the table from which the records will be counted.

## Helpful links
- [SQLite SELECT COUNT](https://www.sqlitetutorial.net/sqlite-select/sqlite-select-count/)

onelinerhub: [How do I count the records in a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-count-the-records-in-a-sqlite-database)