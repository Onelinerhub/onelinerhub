# How to add a user in MongoDB?
// plain

Adding a user in MongoDB is a simple process.

```
use admin
db.createUser({
  user: "username",
  pwd: "password",
  roles: [{ role: "readWrite", db: "databaseName" }]
})
```

The output of the above command should be:
```
Successfully added user: {
	"user" : "username",
	"roles" : [
		{
			"role" : "readWrite",
			"db" : "databaseName"
		}
	]
}
```

## Code explanation

- `use admin`: This command is used to switch to the admin database.
- `db.createUser`: This command is used to create a new user.
- `user`: This is the username of the user.
- `pwd`: This is the password of the user.
- `roles`: This is an array of roles that the user will have.

## Helpful links
- [MongoDB Documentation - Create User](https://docs.mongodb.com/manual/reference/method/db.createUser/)

onelinerhub: [How to add a user in MongoDB?](https://onelinerhub.com/mongodb/how-to-add-a-user-in-mongodb)