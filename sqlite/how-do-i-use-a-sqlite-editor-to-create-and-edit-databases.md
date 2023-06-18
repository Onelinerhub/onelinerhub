# How do I use a SQLite editor to create and edit databases?
// plain

1. Download and install a SQLite editor of your choice. Some popular options include [DB Browser for SQLite](https://sqlitebrowser.org/) and [SQLiteStudio](https://sqlitestudio.pl/index.rvt).

2. Create a new database by clicking the "New Database" button and selecting a location and name for the database.

3. Create tables for the database by clicking the "Execute SQL" tab and entering the following code:

```
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER
);
```

4. Add data to the table using the "Execute SQL" tab and entering the following code:

```
INSERT INTO users (name, age) VALUES ('John', 25);
```

5. Retrieve data from the table using the "Execute SQL" tab and entering the following code:

```
SELECT * FROM users;
```

## Output example

```
id  name  age
1   John  25
```

6. Update data in the table using the "Execute SQL" tab and entering the following code:

```
UPDATE users SET age = 26 WHERE name = 'John';
```

7. Delete data from the table using the "Execute SQL" tab and entering the following code:

```
DELETE FROM users WHERE name = 'John';
```

onelinerhub: [How do I use a SQLite editor to create and edit databases?](https://onelinerhub.com/sqlite/how-do-i-use-a-sqlite-editor-to-create-and-edit-databases)