# How can I change the type of a variable in Rust?
// plain

You can change the type of a variable in Rust by using the `as` keyword. For example, you can cast an `i32` to an `f64` like this:

```rust
let x: i32 = 5;
let y = x as f64;
```

This will output `5.0`.

## Code explanation


- `let x: i32 = 5;`: This declares a variable `x` of type `i32` and assigns it the value `5`.
- `let y = x as f64;`: This casts the value of `x` from `i32` to `f64` and assigns it to the variable `y`.

No relevant links.

group: rust-variables