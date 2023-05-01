# How to match multiple error types in Rust
// plain

Rust provides a powerful way to match multiple error types using the `match` keyword. This allows you to handle different types of errors in a single block of code.

Here is an example of how to match multiple error types in Rust:

```
fn main() {
    let result = do_something();
    match result {
        Ok(value) => println!("Success: {}", value),
        Err(err) => match err {
            Error::IOError(e) => println!("IO Error: {}", e),
            Error::ParseError(e) => println!("Parse Error: {}", e),
            _ => println!("Unknown Error"),
        },
    }
}
```

In this example, the `do_something()` function returns a `Result` type, which can either be an `Ok` value or an `Err` value. If the result is an `Ok` value, it is printed to the console. If the result is an `Err` value, it is matched against different types of errors. In this example, we are matching against `IOError` and `ParseError`. If the error matches either of these types, the appropriate message is printed to the console. If the error does not match either of these types, a generic "Unknown Error" message is printed.

Here is a breakdown of the code:

- `let result = do_something()`: This line calls the `do_something()` function and stores the result in the `result` variable.

- `match result {`: This line starts a `match` block, which is used to match against different types of errors.

- `Ok(value) => println!("Success: {}", value)`: This line matches against `Ok` values and prints a success message to the console.

- `Err(err) => match err {`: This line matches against `Err` values and starts a new `match` block to match against different types of errors.

- `Error::IOError(e) => println!("IO Error: {}", e)`: This line matches against `IOError` and prints an appropriate message to the console.

- `Error::ParseError(e) => println!("Parse Error: {}", e)`: This line matches against `ParseError` and prints an appropriate message to the console.

- `_ => println!("Unknown Error")`: This line matches against any other type of error and prints a generic "Unknown Error" message to the console.

- `}`: This line closes the `match` block.

### Output

Success: <value>

or

IO Error: <error message>

or

Parse Error: <error message>

or

Unknown Error

## Helpful links:

- [Rust Match](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Rust Result](https://doc.rust-lang.org/std/result/)