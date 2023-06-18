# How do I use an SQLite UPDATE statement with a SELECT query?
// plain

An SQLite UPDATE statement with a SELECT query can be used to update multiple rows in a table. The SELECT query must return the rows that are to be updated. The UPDATE statement then updates the values of the columns specified in the statement.

For example, the following statement updates the rows returned by the SELECT query with the value of `'updated'`:

```
UPDATE table_name
SET column_name = 'updated'
WHERE column_name IN (SELECT column_name
                      FROM table_name
                      WHERE condition);
```

This statement will update all rows that meet the condition specified in the SELECT query.

The parts of this statement are as follows:

1. `UPDATE table_name`: This specifies the table in which the rows will be updated.
2. `SET column_name = 'updated'`: This specifies the column that will be updated and the value that it will be updated to.
3. `WHERE column_name IN (SELECT column_name`: This specifies the condition for the SELECT query that returns the rows to be updated.

## Helpful links
- [SQLite UPDATE](https://www.sqlite.org/lang_update.html)
- [SQLite SELECT](https://www.sqlite.org/lang_select.html)

onelinerhub: [How do I use an SQLite UPDATE statement with a SELECT query?](https://onelinerhub.com/sqlite/how-do-i-use-an-sqlite-update-statement-with-a-select-query)