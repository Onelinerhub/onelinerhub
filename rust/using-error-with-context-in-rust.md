# Using error with context in Rust
// plain

, how can I print the line number of an error?



Using the `line!` macro, you can print the line number of an error in Rust. This macro is part of the `std::macros` module. Here is an example of how to use it:

```
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
    let x = 5;
    let y = 0;
    let z = x / y;
    println!("{}", z);
    Ok(())
}
```

This code will produce an error, and the line number of the error can be printed using the `line!` macro:

```
thread 'main' panicked at 'attempt to divide by zero', src/main.rs:7:9
note: Run with `RUST_BACKTRACE=1` environment variable to display a backtrace.
```

Here is a breakdown of the code parts:

- `use std::error::Error;`: This imports the `Error` trait from the `std::error` module.
- `let x = 5;`: This creates a variable `x` with the value `5`.
- `let y = 0;`: This creates a variable `y` with the value `0`.
- `let z = x / y;`: This creates a variable `z` with the value of `x` divided by `y`.
- `println!("{}", z);`: This prints the value of `z` to the console.
- `Ok(())`: This returns an `Ok` result with an empty tuple.
- `thread 'main' panicked at 'attempt to divide by zero', src/main.rs:7:9`: This is the output of the `line!` macro, which prints the line number of the error (in this case, line 7).

External Links:

- [Rust Documentation - Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)
- [Rust Documentation - Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)