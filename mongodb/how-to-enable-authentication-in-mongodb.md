# How to enable authentication in MongoDB?
// plain

MongoDB supports several different methods for authentication.

The most basic authentication method is the **MongoDB Native Authentication**, which uses a username and password to authenticate a user.

To enable authentication in MongoDB, you need to create a user with the `db.createUser()` method.

```
db.createUser(
   {
     user: "myUserAdmin",
     pwd: "abc123",
     roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
   }
)
```

The above example creates a user with the username `myUserAdmin` and the password `abc123`, and assigns the `userAdminAnyDatabase` role to the user.

Once the user is created, you can enable authentication in MongoDB by setting the `auth` parameter to `true` in the `mongod.conf` configuration file.

## Helpful links

- [MongoDB Authentication](https://docs.mongodb.com/manual/core/authentication/)
- [MongoDB Create User](https://docs.mongodb.com/manual/reference/method/db.createUser/)

onelinerhub: [How to enable authentication in MongoDB?](https://onelinerhub.com/mongodb/how-to-enable-authentication-in-mongodb)