# How do I show the databases in SQLite?
// plain

To show the databases in SQLite, you can use the following command:

```
.databases
```

This command will show all the databases that are attached to the current SQLite session. The output of this command will be a list of database names and the main database file associated with each one. For example:

```
seq  main    /path/to/database.db
```

The command `.databases` can also be used to list the attached databases along with their associated files. This is done with the following command:

```
.databases

seq  main    /path/to/database.db
seq  temp    /path/to/temp.db
```

The output of this command will be a list of database names and their associated files.

## Code explanation


1. `.databases` - This command is used to show the databases that are attached to the current SQLite session.
2. `seq` - This is the sequence number of the database.
3. `main` - This is the name of the database.
4. `/path/to/database.db` - This is the path to the database file.

## Helpful links

1. [SQLite Documentation](https://sqlite.org/docs.html)
2. [SQLite .databases Command](https://www.sqlitetutorial.net/sqlite-dot-command/)

onelinerhub: [How do I show the databases in SQLite?](https://onelinerhub.com/sqlite/how-do-i-show-the-databases-in-sqlite)