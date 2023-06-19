# How do I list users on Amazon Redshift?
// plain

To list users on Amazon Redshift, you can use the `pg_user` system view. This view contains information about all users that have been created in the current database.

## Example


```SQL
SELECT usename, usesysid, usecreatedb, usesuper, valuntil
FROM pg_user;
```

## Output example

```
usename  | usesysid | usecreatedb | usesuper | valuntil
---------+----------+-------------+----------+----------
user1    |       10 | t           | t        |
user2    |       11 | t           | f        |
user3    |       12 | f           | f        |
```

The code above will list all the users in the current database, along with their system ID, their ability to create databases, their ability to use superuser privileges, and the expiration date of their account.

## Code explanation


- `SELECT usename, usesysid, usecreatedb, usesuper, valuntil`: This is the SELECT statement that will retrieve the list of users in the current database. The columns specified in this statement are the username, system ID, ability to create databases, ability to use superuser privileges, and expiration date of the account.

- `FROM pg_user`: This is the FROM clause that specifies the source of the data, which is the `pg_user` system view.

## Helpful links

- [Amazon Redshift Documentation - System Views](https://docs.aws.amazon.com/redshift/latest/dg/r_System_views.html)
- [Amazon Redshift Documentation - pg_user System View](https://docs.aws.amazon.com/redshift/latest/dg/r_PG_USER.html)

onelinerhub: [How do I list users on Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-list-users-on-amazon-redshift)