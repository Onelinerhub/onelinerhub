# How to display error in Rust
// plain

Rust provides a standard library module called `std::error` which provides a trait called `Error` that can be used to display errors. The `Error` trait provides a `Display` implementation which can be used to print errors.

## Code example:

```rust
use std::error::Error;

fn main() {
    let err = "Error message";
    let err_obj = err.into();
    println!("{}", err_obj);
}
```

### Output

Error message

## Explanation:

1. The `use std::error::Error` statement imports the `Error` trait from the `std::error` module.

2. The `err` variable is a string literal containing the error message.

3. The `err_obj` variable is created by converting the `err` string literal into an `Error` object using the `into()` method.

4. The `println!` macro is used to print the error message contained in the `err_obj` object.

## Helpful links:

1. [Rust Documentation - std::error](https://doc.rust-lang.org/std/error/)
2. [Rust Documentation - Error Trait](https://doc.rust-lang.org/std/error/trait.Error.html)