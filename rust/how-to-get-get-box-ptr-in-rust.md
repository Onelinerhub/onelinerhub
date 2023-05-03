# How to get get box ptr in Rust
// plain

Getting a pointer to a box in Rust is a simple process. To do this, you need to use the `Box::into_raw` method. This method takes a `Box<T>` and returns a `*mut T`, which is a raw pointer to the box.

```rust
let my_box = Box::new(5);
let my_ptr = Box::into_raw(my_box);
```

The code above creates a `Box<T>` containing the value `5` and then converts it into a raw pointer. The output of this code is a `*mut i32` which is a pointer to the box.

- `Box::new(5)`: creates a `Box<T>` containing the value `5`
- `Box::into_raw(my_box)`: takes a `Box<T>` and returns a `*mut T`, which is a raw pointer to the box

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)

group: rust-box