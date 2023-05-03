# How to disable borrow checker in Rust
// plain

The borrow checker is a feature of the Rust compiler that prevents data races and other memory safety issues. It can be disabled by using the `#[allow(unused_variables)]` attribute on a function or block of code. This will allow the compiler to ignore the borrow checker for that particular function or block of code.

Example:
```rust
#[allow(unused_variables)]
fn foo() {
    let x = 5;
    let y = &x;
    // do something with x and y
}
```

This example will allow the compiler to ignore the borrow checker for the `foo` function, allowing `x` and `y` to be used without any errors.

## Helpful links

- [Rust Reference - Attributes](https://doc.rust-lang.org/reference/attributes.html)
- [Rust Reference - Unused Variables](https://doc.rust-lang.org/reference/attributes/unused_variables.html)

group: rust-borrow