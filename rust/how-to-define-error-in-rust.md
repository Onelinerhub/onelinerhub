# How to define error in Rust
// plain

Error in Rust is defined using the `Result` type, which is an enum that can either be `Ok` or `Err`. `Ok` is used to indicate success, while `Err` is used to indicate an error.

## Code example:

```
fn divide(x: i32, y: i32) -> Result<i32, &'static str> {
    if y == 0 {
        return Err("Cannot divide by zero!");
    }
    Ok(x / y)
}
```

### Output

`Result<i32, &'static str>`

## Explanation of code parts:

1. `fn divide(x: i32, y: i32) -> Result<i32, &'static str>`: This defines a function called `divide` that takes two `i32` parameters and returns a `Result` type with an `i32` type for `Ok` and a `&'static str` type for `Err`.

2. `if y == 0 { return Err("Cannot divide by zero!"); }`: This checks if the second parameter is equal to zero, and if it is, it returns an `Err` with the message "Cannot divide by zero!".

3. `Ok(x / y)`: This returns an `Ok` with the result of the division of the two parameters.

## Helpful links:

1. [Rust Documentation - Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
2. [Rust Documentation - Result](https://doc.rust-lang.org/std/result/)