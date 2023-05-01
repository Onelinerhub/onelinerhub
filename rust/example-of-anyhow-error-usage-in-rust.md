# Example of anyhow error usage in Rust
// plain

The `anyhow` crate is a Rust library for error handling that provides a convenient way to convert errors into a unified error type. It is designed to make it easier to write code that handles errors in a consistent way.

Here is an example of using `anyhow` to handle errors in Rust:

```rust
use anyhow::Result;

fn main() -> Result<()> {
    let result = do_something()?;
    println!("Result: {}", result);
    Ok(())
}

fn do_something() -> Result<i32> {
    let x = 5;
    let y = 0;
    if y == 0 {
        return Err(anyhow!("Division by zero"));
    }
    Ok(x / y)
}
```

### Output

```
thread 'main' panicked at 'Division by zero: anyhow::Error', src/libcore/result.rs:1165:5
```

## Explanation of code parts:

1. `use anyhow::Result;` - This imports the `Result` type from the `anyhow` crate, which is used to return a unified error type.

2. `fn do_something() -> Result<i32> {` - This function returns a `Result<i32>`, which is a type that can either contain a valid `i32` value or an error.

3. `if y == 0 { return Err(anyhow!("Division by zero")); }` - This checks if `y` is equal to zero, and if it is, it returns an error using the `anyhow!` macro.

4. `Ok(x / y)` - If `y` is not equal to zero, this will return the result of the division as an `Ok` value.

## Helpful links:

1. [anyhow crate documentation](https://docs.rs/anyhow/1.0.31/anyhow/)
2. [Rust error handling guide](https://doc.rust-lang.org/book/ch09-00-error-handling.html)