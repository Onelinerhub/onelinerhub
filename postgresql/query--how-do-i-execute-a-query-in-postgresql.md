# query

How do I execute a query in PostgreSQL?
// plain

The following steps outline how to execute a query in PostgreSQL:

1. Connect to the PostgreSQL database:
  ```
  psql -h hostname -d databasename -U username -W
  ```
  This command will prompt for a password for the specified user.

2. Once connected, execute the query:
  ```
  SELECT * FROM table_name;
  ```
  This example query will select all columns from the specified table.

3. After executing the query, the output will be displayed in the terminal:
  ```
  id | name  | age
  ------------------------
  1  | John  | 23
  2  | Sarah | 27
  ```

4. To save the output to a file, use the \o command:
  ```
  \o output.txt
  ```

5. Execute the query again:
  ```
  SELECT * FROM table_name;
  ```
  This will save the output to the output.txt file.

6. To exit the PostgreSQL shell, use the \q command:
  ```
  \q
  ```

7. To view the contents of the output.txt file, use the cat command:
  ```
  cat output.txt
  ```
  This will print the contents of the output.txt file to the terminal.

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [psql Command Line Tool](https://www.postgresql.org/docs/9.2/app-psql.html)

onelinerhub: [query

How do I execute a query in PostgreSQL?](https://onelinerhub.com/postgresql/query--how-do-i-execute-a-query-in-postgresql)