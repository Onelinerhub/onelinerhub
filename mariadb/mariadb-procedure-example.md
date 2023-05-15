# Mariadb procedure example
// plain

A MariaDB stored procedure is a set of SQL statements that can be stored in the server. It can be used to encapsulate a set of operations or logic, which can then be called from multiple client programs.

## Example code

```
CREATE PROCEDURE example_procedure()
BEGIN
  SELECT * FROM table_name;
END;
```

## Output example

```
Query OK, 0 rows affected (0.00 sec)
```

## Code explanation


1. `CREATE PROCEDURE example_procedure()` - This line creates a stored procedure named `example_procedure`.
2. `BEGIN` - This line marks the beginning of the stored procedure.
3. `SELECT * FROM table_name;` - This line selects all the data from the table named `table_name`.
4. `END;` - This line marks the end of the stored procedure.

## Helpful links

- [MariaDB Documentation: Stored Procedures](https://mariadb.com/kb/en/library/stored-procedures/)
- [MariaDB Tutorial: Stored Procedures](https://www.tutorialspoint.com/mariadb/mariadb_stored_procedures.htm)

onelinerhub: [Mariadb procedure example](https://onelinerhub.com/mariadb/mariadb-procedure-example)