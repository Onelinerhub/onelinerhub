# How to list MongoDB users?
// plain

MongoDB users can be listed using the `db.getUsers()` command. This command will return a list of all users in the current database.

## Example

```
> use mydb
switched to db mydb
> db.getUsers()
[
  {
    "_id" : "mydb.user1",
    "user" : "user1",
    "db" : "mydb",
    "roles" : [
        {
            "role" : "readWrite",
            "db" : "mydb"
        }
    ]
  },
  {
    "_id" : "mydb.user2",
    "user" : "user2",
    "db" : "mydb",
    "roles" : [
        {
            "role" : "readWrite",
            "db" : "mydb"
        }
    ]
  }
]
```

## Code explanation

- `db.getUsers()`: command to list all users in the current database

## Helpful links
- [MongoDB Documentation - db.getUsers()](https://docs.mongodb.com/manual/reference/method/db.getUsers/)

onelinerhub: [How to list MongoDB users?](https://onelinerhub.com/mongodb/how-to-list-mongodb-users)