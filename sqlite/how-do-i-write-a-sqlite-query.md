# How do I write a SQLite query?
// plain

Writing a SQLite query is a relatively straightforward process. The syntax of the query is similar to other SQL implementations. The following is an example of a SQLite query that creates a table with three columns:

```
CREATE TABLE test (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);
```

This query creates a table named `test` with three columns: `id`, `name`, and `age`. `id` is an integer primary key, `name` is a text field, and `age` is an integer.

To insert data into the table, you can use the `INSERT` statement:

```
INSERT INTO test (name, age) VALUES ('John', 25);
```

This statement inserts a new row into the table `test` with the name `John` and the age `25`.

To query data from the table, you can use the `SELECT` statement:

```
SELECT * FROM test;

id  name  age
1   John  25
```

This statement returns all the rows in the table `test`.

You can also use `WHERE` clauses and `JOIN` statements to query more complex data.

Here are some useful links for learning more about SQLite queries:

* [SQLite Documentation](https://www.sqlite.org/docs.html)
* [SQLite Tutorial](https://www.tutorialspoint.com/sqlite/)
* [SQLite Cheat Sheet](https://www.cheatography.com/davechild/cheat-sheets/sqlite/)

onelinerhub: [How do I write a SQLite query?](https://onelinerhub.com/sqlite/how-do-i-write-a-sqlite-query)