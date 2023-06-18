# How do I use SQLite KMM to create a database?
// plain

SQLite KMM is an open source, cross-platform library for managing SQLite databases. To create a database with SQLite KMM, you need to first create a SQLite database object and then call the execute() method on it.

## Example code

```
import sqlite3

# Create a database object
db = sqlite3.connect('my_database.db')

# Create the database tables
db.execute('CREATE TABLE users (name TEXT, age INTEGER)')
db.execute('CREATE TABLE posts (title TEXT, content TEXT)')

# Commit the changes
db.commit()
```

This code will create two tables named 'users' and 'posts' in the database file 'my_database.db'.

## Code explanation

- `import sqlite3`: imports the SQLite KMM library
- `db = sqlite3.connect('my_database.db')`: creates a database object connected to the file 'my_database.db'
- `db.execute('CREATE TABLE users (name TEXT, age INTEGER)')`: creates a 'users' table with two columns 'name' and 'age'
- `db.execute('CREATE TABLE posts (title TEXT, content TEXT)')`: creates a 'posts' table with two columns 'title' and 'content'
- `db.commit()`: commits the changes to the database

## Helpful links
- SQLite KMM Documentation: https://sqlitekmm.org/docs/index.html

onelinerhub: [How do I use SQLite KMM to create a database?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-kmm-to-create-a-database)