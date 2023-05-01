# New error in Rust
// plain

The new error in Rust is the `E0308` error. This error occurs when a variable is declared as mutable but not actually used as mutable.

Here is an example of code that would cause this error:

```rust
let mut x = 5;
x = 6;
```

The output of this code would be:

```
error[E0308]: mismatched types
  --> src/main.rs:2:5
   |
2  |     x = 6;
   |     ^^^^^ expected mutable, found immutable
```

Explanation of code parts:

1. `let mut x = 5;` - This line declares a mutable variable `x` and assigns it the value of `5`.
2. `x = 6;` - This line attempts to reassign the value of `x` to `6`.

This code will cause the `E0308` error because the variable `x` was declared as mutable but not used as mutable. To fix this error, the variable `x` must be used as mutable by adding the `mut` keyword before it:

```rust
let mut x = 5;
x = 6; // No error
```

## Helpful links:

1. [Rust Error E0308](https://doc.rust-lang.org/error-index.html#E0308)
2. [Rust Mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)