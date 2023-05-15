# How to list users in Mariadb?
// plain

To list users in MariaDB, you can use the `SELECT` statement with the `USER` table.

```sql
SELECT User, Host FROM mysql.user;
```

This will output a list of users and their associated hosts.

## Code explanation


1. `SELECT` - This is a SQL statement used to select data from a database.
2. `USER` - This is the table in the `mysql` database that contains user information.
3. `User, Host` - These are the columns from the `USER` table that will be selected.

## Helpful links

- [MariaDB Documentation - SELECT Syntax](https://mariadb.com/kb/en/library/select/)
- [MariaDB Documentation - USER Table](https://mariadb.com/kb/en/library/user-table/)

onelinerhub: [How to list users in Mariadb?](https://onelinerhub.com/mariadb/how-to-list-users-in-mariadb)