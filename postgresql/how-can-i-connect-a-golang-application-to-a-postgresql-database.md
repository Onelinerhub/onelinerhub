# How can I connect a Golang application to a PostgreSQL database?
// plain

To connect a Golang application to a PostgreSQL database, you need to use the `database/sql` package. This package provides a generic interface for interacting with databases.

The following example code shows how to connect to a PostgreSQL database:

```go
package main

import (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"
)

func main() {
	db, err := sql.Open("postgres", "user=postgres password=postgres dbname=example_db sslmode=disable")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err)
	}
	fmt.Println("Successfully connected!")
}
```

The code above will output the following:

```
Successfully connected!
```

The code above consists of the following parts:

1. `import` statements: imports the `database/sql` package and the `github.com/lib/pq` package, which is needed for connecting to PostgreSQL.
2. `sql.Open`: opens a connection to the PostgreSQL database.
3. `db.Ping`: tests the connection.
4. `fmt.Println`: prints a success message.

For more information, please see the following links:

- [Go Database/SQL tutorial](https://golang.org/doc/articles/wiki/#tmp_3)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)

onelinerhub: [How can I connect a Golang application to a PostgreSQL database?](https://onelinerhub.com/postgresql/how-can-i-connect-a-golang-application-to-a-postgresql-database)