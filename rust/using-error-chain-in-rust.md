# Using error chain in Rust
// plain

Error chain is a Rust library for creating and managing error types and error handling. It provides a convenient way to define and propagate errors throughout a Rust program.

## Code example:

```rust
use error_chain::error_chain;

error_chain! {
    foreign_links {
        Io(std::io::Error);
        ParseInt(std::num::ParseIntError);
    }
}

fn main() -> Result<()> {
    let result = std::fs::read_to_string("my_file.txt")?;
    let number = result.parse::<i32>()?;
    println!("Number is {}", number);
    Ok(())
}
```

### Output

Number is 42

## Explanation:

1. The `error_chain!` macro is used to define the error types and foreign links.
2. The `foreign_links` section defines the external errors that can be propagated through the error chain. In this example, `std::io::Error` and `std::num::ParseIntError` are defined as foreign links.
3. The `main` function is used to read a file and parse its contents as an integer.
4. The `std::fs::read_to_string` function is used to read the contents of the file into a string. The `?` operator is used to propagate any errors that occur during the read operation.
5. The `parse::<i32>` method is used to parse the string as an integer. The `?` operator is used to propagate any errors that occur during the parse operation.
6. The parsed integer is printed to the console.
7. The `Ok(())` expression is used to indicate that the function has completed successfully.

## Helpful links:

1. [Error Chain Documentation](https://docs.rs/error-chain/0.12.1/error_chain/)
2. [Rust Error Handling Tutorial](https://doc.rust-lang.org/book/ch09-00-error-handling.html)