# How to derive error in Rust
// plain

Error handling in Rust is done using the `Result` type, which is an enum that can either be `Ok` or `Err`. To derive an error in Rust, you can use the `#[derive(Debug)]` attribute on a struct or enum. This will allow you to print out the error message when an error occurs.

## Code example:

```rust
#[derive(Debug)]
enum Error {
    NotFound,
    PermissionDenied,
    ConnectionError,
}

fn main() {
    let result = Err(Error::NotFound);
    println!("{:?}", result);
}
```

### Output

`Err(Error::NotFound)`

Explanation:

1. The `#[derive(Debug)]` attribute is used to enable the `Debug` trait for the `Error` enum. This allows us to print out the error message when an error occurs.

2. The `Error` enum is defined with three variants: `NotFound`, `PermissionDenied`, and `ConnectionError`.

3. The `main` function creates a `Result` with an `Err` variant containing the `Error::NotFound` variant.

4. The `println!` macro is used to print out the `Result`, which will print out the error message.

## Helpful links:

1. [Rust Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)
2. [Rust Derive](https://doc.rust-lang.org/rust-by-example/trait/derive.html)