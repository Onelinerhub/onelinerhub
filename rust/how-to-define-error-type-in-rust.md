# How to define error type in Rust
// plain

Error types in Rust are defined using the `enum` keyword. An example of defining an error type is shown below:

```
enum ErrorType {
    FileError,
    NetworkError,
    ParseError,
}
```

This code defines an `ErrorType` enum with three variants: `FileError`, `NetworkError`, and `ParseError`.

Explanation:

- `enum`: keyword used to define an enum type
- `ErrorType`: name of the enum type
- `FileError`, `NetworkError`, `ParseError`: variants of the enum type, each representing a different type of error

## Helpful links:
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Error Handling in Rust](https://doc.rust-lang.org/book/ch09-00-error-handling.html)