# How to create a user in MongoDB?
// plain

Creating a user in MongoDB is a simple process.

```
use admin
db.createUser({
  user: "username",
  pwd: "password",
  roles: [{ role: "readWrite", db: "myDB" }]
})
```

The above example code creates a user with username and password, and assigns the user the readWrite role on the myDB database.

1. `use admin`: This command switches to the admin database.
2. `db.createUser`: This command creates a new user.
3. `user: "username"`: This specifies the username for the new user.
4. `pwd: "password"`: This specifies the password for the new user.
5. `roles: [{ role: "readWrite", db: "myDB" }]`: This assigns the user the readWrite role on the myDB database.

## Output example

```
Successfully added user: {
	"user" : "username",
	"roles" : [
		{
			"role" : "readWrite",
			"db" : "myDB"
		}
	]
}
```

## Helpful links
- [MongoDB Documentation - Create a User](https://docs.mongodb.com/manual/reference/method/db.createUser/)

onelinerhub: [How to create a user in MongoDB?](https://onelinerhub.com/mongodb/how-to-create-a-user-in-mongodb)