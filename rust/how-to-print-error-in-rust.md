# How to print error in Rust
// plain

Rust provides a standard library macro called `eprintln!` to print errors to the standard error output. This macro is similar to the `println!` macro, but prints to the standard error instead of the standard output.

## Code example:

```
fn main() {
    eprintln!("This is an error message");
}
```

### Output

This is an error message

Explanation:

- `eprintln!`: This is a macro provided by the Rust standard library to print errors to the standard error output.
- `This is an error message`: This is the message that will be printed to the standard error output.

## Helpful links:

- [Rust Documentation - Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)
- [Rust Documentation - println!](https://doc.rust-lang.org/std/macro.println.html)