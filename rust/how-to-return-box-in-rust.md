# How to return box in Rust
// plain

Returning a box in Rust is a way to move a value out of a scope without consuming it. This is done by using the `Box::into_raw` method.

```rust
let x = Box::new(5);
let raw = Box::into_raw(x);
```

The code above creates a new box containing the value `5` and then moves it out of the scope using `Box::into_raw`. The `raw` variable now holds a pointer to the box.

- `Box::new(5)` creates a new box containing the value `5`.
- `Box::into_raw(x)` moves the box out of the scope and returns a pointer to it.

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-box