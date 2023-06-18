# How can I use SQLite in Kodular?
// plain

SQLite is an open-source, serverless, self-contained, and transactional SQL database engine. It can be used in Kodular to store and retrieve data.

To use SQLite in Kodular, you need to install the SQLite extension from the Kodular Store. After installing, you can use the SQLite Database component to access the SQLite database.

The following example shows how to create a table and insert data into it.

```
//Create a table
SQLiteDatabase.ExecuteNonQuery("CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, name TEXT, email TEXT);")

//Insert data into the table
SQLiteDatabase.ExecuteNonQuery("INSERT INTO User(name, email) VALUES('John', 'john@example.com');")
```

The output of the above code will be:
```
1 row(s) affected
```

## Code explanation


1. `SQLiteDatabase.ExecuteNonQuery("CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY, name TEXT, email TEXT);")` - This line of code creates a table named User with three columns, id, name and email.

2. `SQLiteDatabase.ExecuteNonQuery("INSERT INTO User(name, email) VALUES('John', 'john@example.com');")` - This line of code inserts a row into the User table with the values 'John' and 'john@example.com' in the name and email columns respectively.

## Helpful links

- [Kodular SQLite Extension](https://store.kodular.io/extension/com.kodular.sqlite)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How can I use SQLite in Kodular?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-in-kodular)