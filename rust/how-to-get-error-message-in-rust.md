# How to get error message in Rust
// plain

Rust provides a number of ways to get error messages. The most common way is to use the `Result` type. `Result` is an enum that can either be `Ok` or `Err`. If the operation is successful, `Ok` is returned, otherwise `Err` is returned with an error message.

## Code example:

```
let result = some_function();

match result {
    Ok(value) => println!("Success: {}", value),
    Err(err) => println!("Error: {}", err),
}
```

### Output

Success: some_value

## Explanation:

1. The `some_function()` function is called and the result is stored in the `result` variable.
2. The `match` statement is used to check the value of `result`.
3. If `result` is `Ok`, the `println!` macro is used to print the value of `value`.
4. If `result` is `Err`, the `println!` macro is used to print the error message stored in `err`.

## Helpful links:

1. [Rust Documentation - Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
2. [Rust Documentation - The Result Type](https://doc.rust-lang.org/std/result/enum.Result.html)