# How to format error string in Rust
// plain

Error strings in Rust can be formatted using the `format!` macro. This macro allows you to create a formatted string using the same syntax as `println!`.

## Code example:

```
let error_message = format!("Error code {}: {}", error_code, error_description);
```

### Output

`Error code <error_code>: <error_description>`

Explanation:

- `format!`: This is a macro that allows you to create a formatted string using the same syntax as `println!`.
- `error_message`: This is the variable that will store the formatted error string.
- `error_code`: This is the variable that stores the error code.
- `error_description`: This is the variable that stores the error description.

## Helpful links:

- [Rust Documentation - format!](https://doc.rust-lang.org/std/macro.format.html)
- [Rust by Example - format!](https://doc.rust-lang.org/rust-by-example/macros/format.html)