# How to throw an exception in Rust
// plain

Throwing an exception in Rust is done using the `panic!` macro. This macro will cause the program to immediately exit with a message.

## Example code

```
fn main() {
    panic!("Something went wrong!");
}
```

## Output example

```
thread 'main' panicked at 'Something went wrong!', src/main.rs:2:4
```

## Code explanation

- `panic!`: The macro used to throw an exception.
- `Something went wrong!`: The message that will be printed when the exception is thrown.

## Helpful links
- [Rust panic! macro documentation](https://doc.rust-lang.org/std/macro.panic.html)

group: rust-throw