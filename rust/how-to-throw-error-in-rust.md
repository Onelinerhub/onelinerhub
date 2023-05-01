# How to throw error in Rust
// plain

Rust provides the `panic!` macro to throw an error. This macro will cause the program to immediately exit with a message.

## Code example:

```
fn main() {
    panic!("This is an error message");
}
```

### Output

```
thread 'main' panicked at 'This is an error message', src/main.rs:2:4
```

## Explanation:

- `panic!` is a macro provided by Rust that will cause the program to immediately exit with a message.
- The message is provided as an argument to the macro.
- In the example above, the message is `This is an error message`.
- The output shows that the panic occurred on line 2 of the main.rs file.

## Helpful links:

- [Rust Documentation - panic!](https://doc.rust-lang.org/std/macro.panic.html)
- [Rust Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)