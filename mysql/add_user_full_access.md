# Create user with full access to single database

```sql
CREATE USER user@localhost;
GRANT ALL PRIVILEGES ON db.* TO user@localhost IDENTIFIED BY 'pwd';
FLUSH PRIVILEGES;
```

- CREATE USER - creates specified user
- user@localhost - user name and host to attach it to
- GRANT ALL PRIVILEGES - grants any operation for specified user
- ON db.* - database tables (all tables of ```db``` database in our case) we want our user to have access to
- TO user@localhost - user we want to grant access to (our newely created user)
- IDENTIFIED BY 'pwd' - set ```pwd``` password for our user
- FLUSH PRIVILEGES - will make sure new user access is granted instantly
