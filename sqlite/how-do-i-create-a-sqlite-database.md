# How do I create a SQLite database?
// plain

1. Create a new file with the `.db` extension. This will be the SQLite database file.

2. Connect to the database using the `sqlite3` command. For example:

```
sqlite3 mydatabase.db
```

3. Create the tables you need in the database. For example:

```
CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  address TEXT
);
```

4. Insert data into the tables. For example:

```
INSERT INTO customers (name, address) VALUES ('John', '123 Main Street');
```

5. Run queries to retrieve data from the database. For example:

```
SELECT * FROM customers;
```

## Output example


```
id  name    address
1   John    123 Main Street
```

6. Close the connection to the database. For example:

```
.exit
```

7. You can now use the SQLite database file `mydatabase.db` in your application.

## Helpful links
* [SQLite Quick Guide](https://www.tutorialspoint.com/sqlite/sqlite_quick_guide.htm)
* [SQLite Tutorial](https://www.tutorialspoint.com/sqlite/)

onelinerhub: [How do I create a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-create-a-sqlite-database)