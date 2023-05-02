# How to add to pointer in Rust
// plain

In Rust, you can add to a pointer by using the `offset` method. This method takes an integer argument and adds it to the pointer's address. For example, if you have a pointer `ptr` pointing to an integer, you can add 5 to it by using `ptr.offset(5)`. The output of this operation will be a pointer pointing to the integer 5 positions away from the original pointer. You can also use the `offset` method to subtract from a pointer, by passing a negative integer as an argument. For example, `ptr.offset(-5)` will return a pointer pointing to the integer 5 positions before the original pointer.

```rust
let ptr = &mut 5;
let new_ptr = ptr.offset(5);
```

In the example above, `ptr` is a pointer pointing to the integer 5, and `new_ptr` is a pointer pointing to the integer 10 (5 positions away from the original pointer).

## Helpful links
- [Rust Documentation - Pointer Offset](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset)
- [Rust by Example - Pointers](https://doc.rust-lang.org/rust-by-example/std_misc/pointers.html)
- [Rust Book - Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)

group: rust-pointers