# How do I clear a table in SQLite?
// plain

To clear a table in SQLite, you can use the `DELETE` statement. The syntax for this statement is:
```
DELETE FROM <table_name>;
```
where `<table_name>` is the name of the table you want to clear. For example, to clear the `Users` table, the statement would be:
```
DELETE FROM Users;
```

This statement will delete all the rows in the table, but not the table itself. To delete the table, you can use the `DROP TABLE` statement. The syntax for this statement is:
```
DROP TABLE <table_name>;
```
where `<table_name>` is the name of the table you want to delete. For example, to delete the `Users` table, the statement would be:
```
DROP TABLE Users;
```

This statement will delete the table and all the data in it.

## Code explanation
**

1. `DELETE FROM <table_name>;` - statement to delete all rows in a table
2. `DROP TABLE <table_name>;` - statement to delete a table and all its data

**## Helpful links**

1. [SQLite DELETE statement](https://www.sqlite.org/lang_delete.html)
2. [SQLite DROP TABLE statement](https://www.sqlite.org/lang_droptable.html)

onelinerhub: [How do I clear a table in SQLite?](https://onelinerhub.com/sqlite/how-do-i-clear-a-table-in-sqlite)