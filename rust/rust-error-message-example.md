# Rust error message example
// plain

The following is an example of a Rust error message:

```
error[E0425]: cannot find value `x` in this scope
  --> src/main.rs:5:17
   |
5  |     println!("The value of x is: {}", x);
   |                 ^ not found in this scope
```

This error message is telling us that the variable `x` is not found in the current scope. This means that the variable `x` has not been declared or initialized in the current scope.

Explanation of code parts:

- `error[E0425]`: This is the error code for the error message.
- `cannot find value `x` in this scope`: This is the description of the error.
- `src/main.rs:5:17`: This is the location of the error in the source code.
- `println!("The value of x is: {}", x);`: This is the line of code that caused the error.

## Helpful links:

- [Rust Error Index](https://doc.rust-lang.org/error-index.html)
- [Rust Error Handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html)