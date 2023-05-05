# How to throw an error in Rust
// plain

Throwing an error in Rust is done using the `panic!` macro. This macro will cause the program to immediately exit with a message.

## Example code

```rust
fn main() {
    panic!("Something went wrong!");
}
```

## Output example

```
thread 'main' panicked at 'Something went wrong!', src/main.rs:2:4
```

The `panic!` macro takes a single argument, which is a string literal. This string will be printed to the console when the panic occurs.

The `panic!` macro is useful for signaling an unrecoverable error in the program. It should not be used for normal error handling.

## Helpful links
- [The Rust Programming Language - panic!](https://doc.rust-lang.org/std/macro.panic.html)

group: rust-throw