# How do I create a table using SphinxSearch?
// plain

Creating a table using SphinxSearch is a straightforward process. Here is an example of a table creation statement using SphinxSearch:

```
CREATE TABLE tbl_name (
    col_name1 INT NOT NULL,
    col_name2 VARCHAR(255) NOT NULL,
    col_name3 DATETIME NOT NULL
) ENGINE=SPHINX CONNECTION='sphinx://localhost:9306/test';
```

This statement will create a table named `tbl_name` with 3 columns: `col_name1` of type `INT`, `col_name2` of type `VARCHAR(255)` and `col_name3` of type `DATETIME`. The `ENGINE` is set to `SPHINX` and the `CONNECTION` is set to `sphinx://localhost:9306/test`.

The parts of the statement are as follows:

1. `CREATE TABLE`: This is the SQL command to create a new table.
2. `tbl_name`: This is the name of the table to be created.
3. `col_name1 INT NOT NULL`: This is the first column of the table, named `col_name1`, of type `INT` and with the `NOT NULL` constraint.
4. `col_name2 VARCHAR(255) NOT NULL`: This is the second column of the table, named `col_name2`, of type `VARCHAR(255)` and with the `NOT NULL` constraint.
5. `col_name3 DATETIME NOT NULL`: This is the third column of the table, named `col_name3`, of type `DATETIME` and with the `NOT NULL` constraint.
6. `ENGINE=SPHINX`: This sets the engine to `SPHINX` for the table.
7. `CONNECTION='sphinx://localhost:9306/test'`: This sets the connection string to `sphinx://localhost:9306/test` for the table.

For more information, please refer to the [SphinxSearch documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I create a table using SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-create-a-table-using-sphinxsearch)