# How to assert error type in Rust
// plain

In Rust, you can use the `assert_eq!` macro to assert that two values are equal and throw an error if they are not. You can also use the `assert_ne!` macro to assert that two values are not equal and throw an error if they are.

## Code example:

```
let x = 5;
let y = 10;

assert_eq!(x, y);
```

### Output

```
thread 'main' panicked at 'assertion failed: `(left == right)`
  left: `5`,
 right: `10`', src/main.rs:3:5
```

## Explanation:

1. The `let` keyword is used to declare a variable in Rust.
2. The `assert_eq!` macro is used to assert that two values are equal and throw an error if they are not.
3. The `assert_ne!` macro is used to assert that two values are not equal and throw an error if they are.
4. The `panic!` macro is used to throw an error when an assertion fails.

## Helpful links:

1. [Rust Documentation - Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)
2. [Rust Documentation - Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)