# How do I install SQLite on Ubuntu?
// plain

1. Install SQLite3 on Ubuntu using the following command:
```
sudo apt-get install sqlite3
```
2. After installation, check the version of SQLite installed using the following command:
```
sqlite3 --version
```
## Output example

```
3.22.0 2018-01-22 18:45:57 8f7f2d8b0e7c9b8c1f8b2b0fa9a9f2b9
```
3. To create a new database, use the following command:
```
sqlite3 mydb.sqlite
```
4. This will create a new database file called `mydb.sqlite`. You can open this file using the `sqlite3` command.
5. You can also use the `.tables` command to list all the tables in the database.
6. To exit the SQLite prompt, use the `.exit` command.
7. For more information, please refer to the official SQLite documentation: https://www.sqlite.org/docs.html.

onelinerhub: [How do I install SQLite on Ubuntu?](https://onelinerhub.com/sqlite/how-do-i-install-sqlite-on-ubuntu)