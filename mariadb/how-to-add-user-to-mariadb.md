# How to add user to Mariadb?
// plain

Adding a user to MariaDB is a simple process.

1. Log in to the MariaDB server as the root user:
```
mysql -u root -p
```

2. Create a new user with the CREATE USER command:
```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

3. Grant the user privileges with the GRANT command:
```
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';
```

4. Flush the privileges to make sure the changes take effect:
```
FLUSH PRIVILEGES;
```

5. Exit the MariaDB shell:
```
EXIT;
```

The new user is now ready to use.

## Helpful links

- [MariaDB Documentation - Adding User Accounts](https://mariadb.com/kb/en/library/adding-user-accounts/)

onelinerhub: [How to add user to Mariadb?](https://onelinerhub.com/mariadb/how-to-add-user-to-mariadb)