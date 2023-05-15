# Working with JSON in Mariadb
// plain

JSON is a popular data format for storing and exchanging data. MariaDB supports JSON data types, allowing you to store and manipulate JSON documents in MariaDB.

## Example code

```
CREATE TABLE json_table (
  id INT NOT NULL AUTO_INCREMENT,
  json_data JSON,
  PRIMARY KEY (id)
);
```

## Output example

```
Query OK, 0 rows affected (0.02 sec)
```

## Code explanation

- `CREATE TABLE`: This statement creates a new table in the database.
- `json_table`: This is the name of the table being created.
- `id INT NOT NULL AUTO_INCREMENT`: This creates a column called `id` with an integer data type that is not null and automatically increments.
- `json_data JSON`: This creates a column called `json_data` with a JSON data type.
- `PRIMARY KEY (id)`: This sets the `id` column as the primary key for the table.

## Helpful links
- [MariaDB JSON Documentation](https://mariadb.com/kb/en/library/json/)
- [MariaDB CREATE TABLE Documentation](https://mariadb.com/kb/en/library/create-table/)

onelinerhub: [Working with JSON in Mariadb](https://onelinerhub.com/mariadb/working-with-json-in-mariadb)