# How do I use SQLite to update or insert data?
// plain

SQLite is a popular database engine that is used to store and access data. It is a lightweight and powerful database that is easy to use. In order to update or insert data into a SQLite database, you must first create a connection to the database. This can be done using the `sqlite3` module.

Once the connection is established, you can use the `cursor` object to execute SQL statements. To update or insert data, you can use the `execute` method of the `cursor` object.

For example, to insert a new row into a table named `users`, you can use the following code:

```
import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
c = conn.cursor()

# Execute the SQL statement
c.execute("INSERT INTO users (name, email) VALUES ('John', 'john@example.com')")

# Commit the changes
conn.commit()
```

The above code will insert a new row into the `users` table with the name `John` and the email `john@example.com`.

To update existing data in the database, you can use the `UPDATE` statement. For example, to update the email address of the user `John`:

```
import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
c = conn.cursor()

# Execute the SQL statement
c.execute("UPDATE users SET email = 'john@example.net' WHERE name = 'John'")

# Commit the changes
conn.commit()
```

The above code will update the email address of the user `John` to `john@example.net`.

#### List of Code Parts

1. `sqlite3` module: used to create a connection to the database.
2. `cursor` object: used to execute SQL statements.
3. `execute` method: used to update or insert data.
4. `INSERT` statement: used to insert new data into the database.
5. `UPDATE` statement: used to update existing data in the database.

#### Relevant Links

1. [SQLite Python tutorial](https://www.sqlitetutorial.net/sqlite-python/)
2. [SQLite Insert](https://www.sqlitetutorial.net/sqlite-insert/)
3. [SQLite Update](https://www.sqlitetutorial.net/sqlite-update/)

onelinerhub: [How do I use SQLite to update or insert data?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-to-update-or-insert-data)