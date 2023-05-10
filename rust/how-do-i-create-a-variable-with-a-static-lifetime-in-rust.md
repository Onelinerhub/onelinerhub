# How do I create a variable with a static lifetime in Rust?
// plain

A variable with a static lifetime in Rust is one that is valid for the entire duration of the program. This is achieved by declaring the variable with the `static` keyword.

```rust
static VAR: i32 = 5;
```

This declares a variable `VAR` with a static lifetime and an initial value of `5`.

- `static`: keyword used to declare a variable with a static lifetime
- `VAR`: name of the variable
- `i32`: type of the variable
- `5`: initial value of the variable

## Helpful links
- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#variables-and-mutability)

group: rust-variables