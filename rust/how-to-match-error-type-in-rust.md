# How to match error type in Rust
// plain

Rust provides a powerful way to match errors using the `match` keyword. This allows you to handle different types of errors in different ways.

Below is an example of how to match an error type in Rust:

```
fn main() {
    let result = some_function();
    match result {
        Ok(value) => println!("Got a value: {}", value),
        Err(err) => match err.kind() {
            ErrorKind::NotFound => println!("Not found"),
            ErrorKind::PermissionDenied => println!("Permission denied"),
            _ => println!("Other error"),
        },
    }
}
```

### Output

Got a value: 10

In this example, the `match` keyword is used to match the result of the `some_function()` call. If the result is `Ok`, then the value is printed. If the result is `Err`, then the `kind()` method is used to match the type of error. Depending on the type of error, a different message is printed.

Explanation of code parts:

1. `let result = some_function();` - This line declares a variable `result` and assigns it the result of the `some_function()` call.
2. `match result {` - This line starts a `match` block which is used to match the result of the `some_function()` call.
3. `Ok(value) => println!("Got a value: {}", value),` - This line matches the `Ok` variant of the `result` variable and prints the value.
4. `Err(err) => match err.kind() {` - This line matches the `Err` variant of the `result` variable and starts a `match` block to match the type of error.
5. `ErrorKind::NotFound => println!("Not found"),` - This line matches the `ErrorKind::NotFound` variant and prints the message "Not found".
6. `ErrorKind::PermissionDenied => println!("Permission denied"),` - This line matches the `ErrorKind::PermissionDenied` variant and prints the message "Permission denied".
7. `_ => println!("Other error"),` - This line matches any other variant and prints the message "Other error".

## Helpful links:

1. [Rust Match](https://doc.rust-lang.org/book/ch06-02-match.html)
2. [Rust Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)