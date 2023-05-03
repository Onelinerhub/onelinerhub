# How to drop box in Rust
// plain

Dropping a box in Rust is a way to deallocate memory that is no longer needed. This is done by calling the `drop` function on the box.

```rust
let mut x = Box::new(5);
drop(x);
```

The code above creates a box containing the value 5 and then calls the `drop` function on it. This will deallocate the memory that was allocated for the box.

The `drop` function takes a mutable reference to the box as an argument. This is necessary because the `drop` function needs to modify the box in order to deallocate the memory.

The `drop` function is a special function that is automatically called when a box is no longer needed. This ensures that the memory allocated for the box is deallocated and not left to waste.

## Helpful links

- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust Documentation - Drop](https://doc.rust-lang.org/std/ops/trait.Drop.html)

group: rust-box