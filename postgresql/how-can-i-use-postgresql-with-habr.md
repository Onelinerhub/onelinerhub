# How can I use PostgreSQL with Habr?
// plain

PostgreSQL and Habr can be used together to store and query data. PostgreSQL is an open source object-relational database management system (ORDBMS) that provides a powerful and feature-rich platform for data storage and retrieval.

The following example shows how to connect to a PostgreSQL database from the Habr platform:

```
// Connect to the PostgreSQL database
$conn = pg_connect("host=localhost port=5432 dbname=mydb user=postgres password=mypass");

// Execute a query
$result = pg_query($conn, "SELECT * FROM mytable");

// Output the results
while ($row = pg_fetch_row($result)) {
  echo "Name: $row[0]  Email: $row[1]";
}
```

The code above will connect to a PostgreSQL database and execute a query to retrieve data from a table named `mytable`. The results will be outputted as a list of names and emails.

The following are some of the parts of the code explained:

- `pg_connect()` – establishes a connection to a PostgreSQL database.
- `pg_query()` – executes a query against the database.
- `pg_fetch_row()` – fetches a row from the query result.

For more information on using PostgreSQL with Habr, please refer to the following links:

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Habr PostgreSQL Tutorial](https://habr.com/en/post/453614/)

onelinerhub: [How can I use PostgreSQL with Habr?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-with-habr)