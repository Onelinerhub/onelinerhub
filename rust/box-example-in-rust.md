# Box example in Rust
// plain

Rust is a programming language that is designed to be fast, safe, and concurrent. It is a statically typed language that uses type inference to make code more concise and readable.

A box is a data structure that allows you to store a value in a single memory location. It is a type of pointer that can be used to store any type of data.

Example code:
```rust
let x = Box::new(5);
```

Output:
```
Box { value: 5 }
```

Code parts:
- `let x =`: declares a variable `x`
- `Box::new(5)`: creates a new box containing the value `5`

## Helpful links
- [Rust Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-box