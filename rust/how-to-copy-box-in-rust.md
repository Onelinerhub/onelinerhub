# How to copy box in Rust
// plain

Copying a box in Rust is a simple process. To do so, use the `clone()` method on the box. This will create a deep copy of the box and its contents.

Example:
```rust
let a = Box::new(5);
let b = a.clone();
```

Output:
```
()
```

Code parts:
- `let a = Box::new(5);`: Creates a new box containing the value 5.
- `let b = a.clone();`: Creates a deep copy of the box `a` and assigns it to `b`.

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-box