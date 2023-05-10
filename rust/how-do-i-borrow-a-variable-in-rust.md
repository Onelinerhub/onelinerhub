# How do I borrow a variable in Rust?
// plain

In Rust, variables can be borrowed using the `&` operator. This operator creates a reference to the variable, allowing it to be used without taking ownership of it.

For example:
```rust
let x = 5;
let y = &x;
```
This code creates a reference `y` to the variable `x`, which has the value `5`.

The parts of this code are:
- `let x = 5;`: This declares a variable `x` with the value `5`.
- `let y = &x;`: This creates a reference `y` to the variable `x`.

For more information, see the [Rust Reference](https://doc.rust-lang.org/reference/index.html).

group: rust-variables