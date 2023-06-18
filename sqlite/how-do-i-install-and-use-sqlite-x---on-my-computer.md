# How do I install and use SQLite x64 on my computer?
// plain

1. Download the [pre-compiled binaries](https://www.sqlite.org/download.html) for your operating system.
2. Extract the files to a directory of your choice.
3. Open a command prompt and navigate to the directory containing the extracted files.
4. To create a new database, enter the following command:

```
sqlite3 mydatabase.db
```

This will create a new database file named `mydatabase.db` in the current directory.
5. To execute a SQL statement, enter the following command:

```
sqlite> CREATE TABLE mytable (id INTEGER PRIMARY KEY, name TEXT);
```

This will create a new table named `mytable` with two columns: `id` and `name`.
6. To view the contents of the table, enter the following command:

```
sqlite> SELECT * FROM mytable;
```

This will return an empty result set.
7. To exit the SQLite shell, enter the following command:

```
sqlite> .exit
```

onelinerhub: [How do I install and use SQLite x64 on my computer?](https://onelinerhub.com/sqlite/how-do-i-install-and-use-sqlite-x---on-my-computer)