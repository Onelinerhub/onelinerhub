# How can I query a SQLite database in a case insensitive manner?
// plain

To query a SQLite database in a case insensitive manner, one can use the `LIKE` operator with the `COLLATE NOCASE` option. This allows for the comparison of strings to be done in a case insensitive way. For example, the following query will return all the entries in the `users` table whose first names start with the letter 'a':

```sql
SELECT * FROM users
WHERE first_name LIKE 'a%' COLLATE NOCASE;
```

The output of this query would be something like:

```
id | first_name | last_name
--------------------------------
1  | Alice      | Smith
2  | Adam       | Johnson
3  | Anthony    | Anderson
```

The parts of the query are as follows:

* `SELECT * FROM users` - This is the standard SQL query syntax to select all entries from the `users` table.
* `WHERE first_name LIKE 'a%'` - This is the condition to filter the entries whose first name starts with the letter 'a'.
* `COLLATE NOCASE` - This is the option to make the comparison of strings case insensitive.

For more information on how to query a SQLite database, see the following links:

* [SQLite Query Language](https://www.sqlite.org/lang.html)
* [Using the LIKE Operator](https://www.sqlitetutorial.net/sqlite-like/)
* [Collation and Collating Sequences](https://www.sqlite.org/lang_collate.html)

onelinerhub: [How can I query a SQLite database in a case insensitive manner?](https://onelinerhub.com/sqlite/how-can-i-query-a-sqlite-database-in-a-case-insensitive-manner)