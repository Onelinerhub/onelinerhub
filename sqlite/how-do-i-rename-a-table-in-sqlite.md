# How do I rename a table in SQLite?
// plain

Renaming a table in SQLite is easy and can be done with the `ALTER TABLE` command. The basic syntax for renaming a table is:
```
ALTER TABLE old_table_name
RENAME TO new_table_name;
```

In the above example, `old_table_name` is the name of the table to be renamed, and `new_table_name` is the new name of the table.

For example, let's say we have a table called `tbl_employees` and we want to rename it to `tbl_staff`. We can do this with the following command:
```
ALTER TABLE tbl_employees
RENAME TO tbl_staff;
```

The output of this command will be:
```
Table tbl_employees renamed to tbl_staff
```

#### List of code parts
1. `ALTER TABLE` - The command used to rename a table in SQLite
2. `old_table_name` - The name of the table to be renamed
3. `RENAME TO` - The keyword used to specify the new name of the table
4. `new_table_name` - The new name of the table

#### Relevant Links
1. [SQLite ALTER TABLE](https://www.sqlite.org/lang_altertable.html)
2. [SQLite Rename Table](https://www.sqlitetutorial.net/sqlite-rename-table/)

onelinerhub: [How do I rename a table in SQLite?](https://onelinerhub.com/sqlite/how-do-i-rename-a-table-in-sqlite)