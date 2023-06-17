# How do I change a user's password in PostgreSQL?
// plain

To change a user's password in PostgreSQL, you can use the `ALTER USER` command.

## Example code

```
ALTER USER username WITH PASSWORD 'new_password';
```

This code will change the password for the user `username` to `new_password`.

## Code explanation

- `ALTER USER`: the command used to change a user's password in PostgreSQL
- `username`: the username of the user whose password you want to change
- `WITH PASSWORD`: keyword used to specify the new password
- `'new_password'`: the new password for the user

## Helpful links
- [PostgreSQL ALTER USER documentation](https://www.postgresql.org/docs/9.4/sql-alteruser.html)

onelinerhub: [How do I change a user's password in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-change-a-user-s-password-in-postgresql)