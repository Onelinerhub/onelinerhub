# How to return error in Rust
// plain

Rust provides a number of ways to return errors. The most common way is to use the `Result` type. `Result` is an enum that can either be `Ok` or `Err`. `Ok` is used to indicate success and `Err` is used to indicate an error.

## Code example:

```
fn divide(x: i32, y: i32) -> Result<i32, &'static str> {
    if y == 0 {
        return Err("Cannot divide by zero!");
    }
    Ok(x / y)
}

fn main() {
    let result = divide(10, 0);
    match result {
        Ok(val) => println!("Result: {}", val),
        Err(err) => println!("Error: {}", err),
    }
}
```

### Output

```
Error: Cannot divide by zero!
```

## Explanation:

1. The `divide` function takes two `i32` parameters and returns a `Result` type. The `Result` type is an enum that can either be `Ok` or `Err`.
2. If the second parameter is 0, the function returns an `Err` with the message "Cannot divide by zero!".
3. If the second parameter is not 0, the function returns an `Ok` with the result of the division.
4. In the `main` function, the result of the `divide` function is stored in the `result` variable.
5. The `match` statement is used to check the value of the `result` variable.
6. If the `result` is `Ok`, the value is printed.
7. If the `result` is `Err`, the error message is printed.

## Helpful links:

1. [Rust Documentation - Result](https://doc.rust-lang.org/std/result/)
2. [Rust Documentation - Match](https://doc.rust-lang.org/book/ch06-02-match.html)