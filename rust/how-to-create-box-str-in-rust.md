# How to create box str in Rust
// plain

Creating a box str in Rust is a simple process. To do so, you need to use the `Box::new()` function. This function takes a value and returns a pointer to a newly allocated value on the heap.

```rust
let my_str = Box::new("Hello World!");
```

The code above creates a `Box` containing a `&str` with the value `"Hello World!"`.

The code consists of the following parts:

- `let`: This is a keyword used to declare a variable.
- `my_str`: This is the name of the variable.
- `Box::new()`: This is a function that takes a value and returns a pointer to a newly allocated value on the heap.
- `"Hello World!"`: This is the value that is passed to the `Box::new()` function.

## Helpful links

- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-box