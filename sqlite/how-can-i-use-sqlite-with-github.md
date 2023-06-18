# How can I use SQLite with Github?
// plain

SQLite can be used with Github by creating a SQLite database file and adding it to a Github repository. To do this, the file must be added to the repository and committed.

For example, to create a SQLite database file called `my_database.db` and add it to a Github repository, the following code can be used:

```
sqlite3 my_database.db
.databases
```

The output of this code would be:

```
0: main: /my_database.db
```

This indicates that the database file has been created. To add it to the Github repository, the following commands can be used:

```
git add my_database.db
git commit -m "Added my_database.db"
git push origin master
```

The `git add` command adds the file to the repository, the `git commit` command commits the changes, and the `git push` command pushes the changes to the remote repository.

## Code explanation

1. `sqlite3 my_database.db` - creates a SQLite database file called `my_database.db`
2. `.databases` - checks if the database file was created
3. `git add my_database.db` - adds the file to the repository
4. `git commit -m "Added my_database.db"` - commits the changes
5. `git push origin master` - pushes the changes to the remote repository

## Helpful links
- [SQLite documentation](https://sqlite.org/docs.html)
- [GitHub documentation](https://docs.github.com/en/github)

onelinerhub: [How can I use SQLite with Github?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-github)