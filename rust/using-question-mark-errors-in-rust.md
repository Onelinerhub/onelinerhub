# Using question mark errors in Rust
// plain

Rust uses the question mark operator (`?`) to handle errors in a concise and easy-to-read way. This operator is used to return a `Result` type, which can either be `Ok` or `Err`.

## Code example:
```
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

## Explanation:
- `fn main()`: This is the main function, which is the entry point of the program.
- `let result = divide(4, 2)`: This line calls the `divide` function with the arguments `4` and `2`.
- `match result {`: This line uses a `match` expression to check the result of the `divide` function.
- `Ok(val) => println!("Result: {}", val)`: If the result is `Ok`, this line prints the value of `val`.
- `Err(e) => println!("Error: {}", e)`: If the result is `Err`, this line prints the value of `e`.
- `fn divide(x: i32, y: i32) -> Result<i32, &'static str>`: This is the `divide` function, which takes two `i32` arguments and returns a `Result` type.
- `if y == 0 {`: This line checks if the second argument is `0`.
- `return Err("Cannot divide by 0")`: If the second argument is `0`, this line returns an `Err` with the message `Cannot divide by 0`.
- `Ok(x / y)`: If the second argument is not `0`, this line returns an `Ok` with the result of the division.

## Helpful links:
- [Rust Documentation - Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
- [Rust Documentation - The Question Mark Operator](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#the-question-mark-operator)