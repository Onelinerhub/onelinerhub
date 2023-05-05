# How to throw custom error in Rust
// plain

Rust provides the `panic!` macro to throw custom errors. It takes a `&str` argument which is the error message.

## Example code

```rust
fn main() {
    panic!("Custom error message");
}
```
## Output example

```
thread 'main' panicked at 'Custom error message', src/main.rs:2:5
```

The code consists of:
- `panic!` macro: used to throw a custom error
- `&str` argument: the error message

## Helpful links
- [Rust panic! macro](https://doc.rust-lang.org/std/macro.panic.html)

group: rust-throw