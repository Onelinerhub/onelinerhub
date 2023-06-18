# How do I use SQLite with Golang?
// plain

SQLite is a popular, lightweight database engine that can be easily used with Golang. To use SQLite with Golang, you need to install the sqlite3 package first. You can do this using the go get command:

```
go get github.com/mattn/go-sqlite3
```

To use the package, you need to import it in your code:

```
import "github.com/mattn/go-sqlite3"
```

Then, you can use the package to open a connection to an existing SQLite database. For example, to open a connection to a database file called "mydb.db":

```
db, err := sql.Open("sqlite3", "mydb.db")
if err != nil {
    log.Fatal(err)
}
```

From there, you can use the standard database/sql package to query and manipulate the database. For example, to execute a SELECT query:

```
rows, err := db.Query("SELECT name FROM users")
if err != nil {
    log.Fatal(err)
}
defer rows.Close()
```

Finally, you can use the rows object to iterate over the results and do something with them:

```
var name string
for rows.Next() {
    err := rows.Scan(&name)
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(name)
}
```

Parts of the code explained:

- `go get github.com/mattn/go-sqlite3`: This command downloads and installs the sqlite3 package.

- `import "github.com/mattn/go-sqlite3"`: This imports the package into your code.

- `db, err := sql.Open("sqlite3", "mydb.db")`: This opens a connection to the database file "mydb.db".

- `rows, err := db.Query("SELECT name FROM users")`: This executes a SELECT query on the database.

- `rows.Scan(&name)`: This reads the results of the query into the variable `name`.

- `fmt.Println(name)`: This prints the value of the `name` variable.

## Helpful links
- [Go SQLite3 Documentation](https://github.com/mattn/go-sqlite3#documentation)
- [Go Database/SQL Documentation](https://golang.org/pkg/database/sql/)

onelinerhub: [How do I use SQLite with Golang?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-with-golang)