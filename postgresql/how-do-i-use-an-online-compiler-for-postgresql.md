# How do I use an online compiler for PostgreSQL?
// plain

Using an online compiler for PostgreSQL is a great way to quickly test out code snippets without needing to install PostgreSQL on a local machine.

The following example code snippet uses the PostgreSQL online compiler to create a table called `table1` and insert data into it:

```
CREATE TABLE table1 (
  id serial PRIMARY KEY,
  name VARCHAR (50),
  age INTEGER
);

INSERT INTO table1 (name, age)
VALUES ('John', 30);

SELECT * FROM table1;
```

The output of this code would look like:

```
 id |  name  | age
----+--------+-----
  1 | John   |  30
(1 row)
```

To use an online compiler for PostgreSQL, you need to:
1. Open an online PostgreSQL compiler such as [SQL Fiddle](http://sqlfiddle.com/#!17/b3c3c/1)
2. Enter your PostgreSQL code in the `Schema` text box
3. Click `Build Schema`
4. Enter any data you want to insert in the `Data` text box
5. Click `Run SQL`

You can also use the online compiler to view the output of queries and view the structure of your tables.

## Helpful links
- [SQL Fiddle](http://sqlfiddle.com/#!17/b3c3c/1)
- [SQL Fiddle Tutorial](https://www.tutorialspoint.com/sqlfiddle)

onelinerhub: [How do I use an online compiler for PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-use-an-online-compiler-for-postgresql)