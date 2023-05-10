# How do I declare a variable outside a function in Rust?
// plain

Variables declared outside a function in Rust are called `static variables`. They are declared using the `static` keyword followed by the type of the variable and the name of the variable.

```rust
static VARIABLE_NAME: TYPE = VALUE;
```

For example,

```rust
static MY_VARIABLE: i32 = 10;
```

This declares a static variable `MY_VARIABLE` of type `i32` with the value `10`.

- `static`: keyword used to declare a static variable
- `MY_VARIABLE`: name of the variable
- `i32`: type of the variable
- `10`: value of the variable

## Helpful links
- [Rust Documentation - Variables](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)

group: rust-variables