# Add new user

```sql
CREATE USER user1 HOST IP '127.0.0.1' IDENTIFIED WITH sha256_password BY 'pwd';
```


group: users

## Example: 
```sql
CREATE USER user1 HOST IP '127.0.0.1' IDENTIFIED WITH sha256_password BY 'pwd';
```
```
CREATE USER user1 IDENTIFIED WITH sha256_hash BY 'A1159E9DF3670D549D04524532629F5477CEB7DEEC9B45E47E8C009506ECB2C8' HOST LOCAL

Query id: bbc7641a-e510-4327-b90c-84a0d52ddbb4

Ok.

0 rows in set. Elapsed: 0.001 sec.
```

