# How to catch error in Rust
// plain

Rust provides a number of ways to catch errors. The most common way is to use the `Result` type. `Result` is an enum that can either be `Ok` or `Err`. `Ok` is used to indicate success and `Err` is used to indicate an error.

## Code example:
```rust
fn main() {
    let result = divide(4, 2);
    match result {
        Ok(val) => println!("Result: {}", val),
        Err(e) => println!("Error: {}", e),
    }
}

fn divide(x: i32, y: i32) -> Result<i32, &'static str> {
    if y == 0 {
        return Err("Cannot divide by 0");
    }
    Ok(x / y)
}
```

### Output
Result: 2

Explanation:
1. The `divide` function takes two `i32` parameters and returns a `Result` type.
2. The `Result` type is an enum that can either be `Ok` or `Err`.
3. If the `y` parameter is 0, the `Err` variant is returned with an error message.
4. If the `y` parameter is not 0, the `Ok` variant is returned with the result of the division.
5. The `match` statement is used to check the `Result` type and print the appropriate message.
6. If the `Result` is `Ok`, the value is printed.
7. If the `Result` is `Err`, the error message is printed.

## Helpful links:
1. [Rust Documentation - Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
2. [Rust Documentation - Result](https://doc.rust-lang.org/std/result/)