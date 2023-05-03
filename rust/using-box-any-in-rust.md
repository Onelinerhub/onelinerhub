# Using box any in Rust
// plain

Box is a type of pointer in Rust that allows you to store data on the heap rather than the stack. It is a type of smart pointer that can be used to store data of any type.

Example code:
```rust
let x = Box::new(5);
```

Output:
```
Box(5)
```

Code parts:
- `let x =`: declares a variable `x`
- `Box::new(5)`: creates a new box containing the value `5`

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust by Example - Box](https://doc.rust-lang.org/rust-by-example/std/box.html)

group: rust-box