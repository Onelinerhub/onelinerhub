# How do I create a variable on the heap in Rust?
// plain

Creating a variable on the heap in Rust is done using the `Box` type. `Box` is a smart pointer that allocates memory on the heap and deallocates it when it goes out of scope.

```rust
let b = Box::new(5);
```

This code creates a `Box` containing the value `5` on the heap.

## Code explanation


1. `let b =` - declares a variable `b`
2. `Box::new(5)` - creates a `Box` containing the value `5` on the heap

## Helpful links

- [Rust Book - Box](https://doc.rust-lang.org/book/ch15-01-box.html)

group: rust-variables