# Using box from_raw in Rust
// plain

`from_raw` is a function in Rust that creates a `Box` from a raw pointer. It takes a raw pointer and a destructor as arguments and returns a `Box` containing the data pointed to by the raw pointer.

Example:
```rust
let ptr = Box::into_raw(Box::new(5));
let boxed = unsafe { Box::from_raw(ptr) };
```
Output: `boxed` is a `Box` containing the value `5`.

Code parts:
- `Box::into_raw(Box::new(5))`: This creates a `Box` containing the value `5` and returns a raw pointer to the data.
- `unsafe { Box::from_raw(ptr) }`: This creates a `Box` from the raw pointer `ptr` and returns it.

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust Documentation - from_raw](https://doc.rust-lang.org/std/boxed/struct.Box.html#method.from_raw)

group: rust-box