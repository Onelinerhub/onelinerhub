# Add new user

```sql
CREATE USER user1 HOST IP '127.0.0.1' IDENTIFIED WITH sha256_password BY 'pwd';
```

- `CREATE USER` - create new user
- `user1` - name of the user to create
- `127.0.0.1` - allow access from localhost only
- `pwd` - password to user for new user

group: users

## Example: 
```sql
CREATE USER user1 HOST IP '127.0.0.1' IDENTIFIED WITH sha256_password BY 'pwd';
```
```
Query id: bbc7641a-e510-4327-b90c-84a0d52ddbb4

Ok.

0 rows in set. Elapsed: 0.001 sec.
```

link_youtube: https://youtu.be/olYfLRs9v_g
