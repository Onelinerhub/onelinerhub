# How to use boxed errors in Rust
// plain

Boxed errors in Rust are a way to handle errors in a more structured way. It allows you to store errors in a box, which can then be used to propagate the error up the call stack. This makes it easier to handle errors in a more organized way.

Here is an example of how to use boxed errors in Rust:

```rust
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let result = do_something()?;
    println!("Result: {}", result);
    Ok(())
}

fn do_something() -> Result<i32, Box<dyn Error>> {
    let result = 10;
    Ok(result)
}
```

### Output

Result: 10

## Explanation of code parts:

1. `use std::error::Error;`: This imports the Error trait from the standard library, which is needed for using boxed errors.

2. `fn main() -> Result<(), Box<dyn Error>> {`: This is the main function, which returns a Result type with an empty tuple as the success type and a Box of a dynamic Error type as the error type.

3. `let result = do_something()?;`: This line calls the do_something() function and uses the ? operator to propagate any errors that occur up the call stack.

4. `fn do_something() -> Result<i32, Box<dyn Error>> {`: This is the do_something() function, which returns a Result type with an i32 as the success type and a Box of a dynamic Error type as the error type.

5. `let result = 10;`: This line assigns the value 10 to the result variable.

6. `Ok(result)`: This line returns the result variable as a success value in the Result type.

## Helpful links:

1. https://doc.rust-lang.org/std/error/trait.Error.html
2. https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html