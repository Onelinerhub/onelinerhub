# How can I quickly get started with SQLite?
// plain

To quickly get started with SQLite, follow these steps:

1. Download and install the SQLite3 command line tool. It can be found [here](https://www.sqlite.org/download.html).

2. Create a database file. This can be done with the following command:
```
sqlite3 mydatabase.db
```

3. Create a table in the database. This can be done with the following command:
```
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT
);
```

4. Insert some data into the table. This can be done with the following command:
```
INSERT INTO users (username, email) VALUES ('John', 'john@example.com');
```

5. Query the data from the table. This can be done with the following command:
```
SELECT * FROM users;
```
This will print out the following output:
```
1|John|john@example.com
```

6. Close the database connection. This can be done with the following command:
```
.exit
```

7. For more information on working with SQLite, check out the [SQLite Tutorial](https://www.sqlitetutorial.net/sqlite-tutorial/).

onelinerhub: [How can I quickly get started with SQLite?](https://onelinerhub.com/sqlite/how-can-i-quickly-get-started-with-sqlite)