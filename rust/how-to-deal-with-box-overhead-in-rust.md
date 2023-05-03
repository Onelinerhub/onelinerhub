# How to deal with box overhead in Rust
// plain

Box overhead in Rust is the cost of allocating memory on the heap for a type. It is necessary to use boxes when dealing with types that have a size unknown at compile time, such as a `Vec<T>`.

Example code:
```rust
let x = Box::new(5);
```

Output:
```
Box { pointer: 0x7f8f9f9f9f9f }
```

The code above creates a box containing the value `5`. The output is a pointer to the memory location of the box.

To avoid box overhead, it is possible to use `Rc<T>` or `Arc<T>` instead of `Box<T>`. These types are reference counted pointers that allow multiple references to the same data without allocating memory on the heap.

## Helpful links
- [Box<T>](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rc<T>](https://doc.rust-lang.org/std/rc/struct.Rc.html)
- [Arc<T>](https://doc.rust-lang.org/std/sync/struct.Arc.html)

group: rust-box