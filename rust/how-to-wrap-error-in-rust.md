# How to wrap error in Rust
// plain

Error wrapping in Rust is a way to handle errors in a more organized and structured way. It allows you to create custom error types that can be used to represent different types of errors. This makes it easier to debug and handle errors in your code.

To wrap an error in Rust, you can use the `Result` type. This type is used to represent the result of a computation that may either succeed or fail. It has two variants, `Ok` and `Err`, which represent the success and failure cases respectively.

## Code example:

```rust
fn divide(x: i32, y: i32) -> Result<i32, String> {
    if y == 0 {
        return Err(String::from("Cannot divide by zero"));
    }
    Ok(x / y)
}

let result = divide(10, 0);

match result {
    Ok(val) => println!("Result: {}", val),
    Err(err) => println!("Error: {}", err),
}
```

### Output

Error: Cannot divide by zero

## Explanation:

- `fn divide(x: i32, y: i32) -> Result<i32, String>`: This is the function signature for the `divide` function. It takes two `i32` parameters and returns a `Result` type with an `i32` for the success case and a `String` for the failure case.

- `if y == 0 { return Err(String::from("Cannot divide by zero")); }`: This is a conditional statement that checks if the second parameter is equal to zero. If it is, it returns an `Err` variant with an error message.

- `Ok(x / y)`: This is the success case for the `divide` function. It returns an `Ok` variant with the result of the division.

- `let result = divide(10, 0);`: This is how we call the `divide` function and store the result in a variable.

- `match result { Ok(val) => println!("Result: {}", val), Err(err) => println!("Error: {}", err), }`: This is a `match` expression that is used to handle the result of the `divide` function. If the result is an `Ok` variant, it prints the result. If the result is an `Err` variant, it prints the error message.

## Helpful links:

- [Rust Documentation - Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [Rust by Example - Error Handling](https://doc.rust-lang.org/rust-by-example/error.html)