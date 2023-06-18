# How can I use SQLite with Rust?
// plain

SQLite is a popular, lightweight, open-source SQL database that can be used with Rust. To use SQLite with Rust, you need to install the sqlx crate.

```
[dependencies]
sqlx = "0.3.2"
```

Once installed, you can use the sqlx crate to connect to an SQLite database, execute queries, and perform other database operations.

```
use sqlx::sqlite::SqlitePool;

#[async_std::main]
async fn main() -> Result<(), sqlx::Error> {
    let pool = SqlitePool::builder()
        .max_size(5)
        .build("sqlite://./my.db")
        .await?;

    let row = sqlx::query!("SELECT * FROM users WHERE id = ?")
        .bind(1)
        .fetch_one(&pool)
        .await?;

    println!("{:?}", row);

    Ok(())
}
```

The code above will connect to an SQLite database, execute a query to select a row from the users table, and print the row.

1. `use sqlx::sqlite::SqlitePool;` - imports the SqlitePool type from the sqlx crate.
2. `SqlitePool::builder()` - creates a new connection pool builder.
3. `.max_size(5)` - sets the maximum size of the connection pool.
4. `.build("sqlite://./my.db")` - builds the connection pool using the provided URL.
5. `sqlx::query!("SELECT * FROM users WHERE id = ?")` - creates a query that will select a row from the users table.
6. `.bind(1)` - binds the value 1 to the query.
7. `.fetch_one(&pool)` - executes the query using the connection pool.
8. `println!("{:?}", row);` - prints the selected row.

## Helpful links
- [sqlx Documentation](https://docs.rs/sqlx/0.3.2/sqlx/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

onelinerhub: [How can I use SQLite with Rust?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-rust)