# Create user with root privileges

```sql
CREATE USER user@localhost IDENTIFIED BY 'pwd';
GRANT ALL PRIVILEGES ON *.* TO user@localhost WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

- `CREATE USER` - creates specified user
- `user@localhost` - user name and host to attach it to
- `GRANT ALL PRIVILEGES` - grants any operation for specified user
- `ON *.*` - allow access to all tables of all databases
- `TO user@localhost` - user we want to grant access to (our newely created user)
- `IDENTIFIED BY 'pwd'` - set `pwd` password for our user
- `FLUSH PRIVILEGES` - will make sure new user access is granted instantly
- `WITH GRANT OPTION` - allow user to grant access to other users

group: create_user


