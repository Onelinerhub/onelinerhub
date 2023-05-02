# How to cast pointer to usize in Rust
// plain

In Rust, you can cast a pointer to a usize using the `as usize` syntax. For example, if you have a pointer `ptr` of type `*const i32`, you can cast it to a usize with `let usize_ptr = ptr as usize`. The output of this code will be a usize that contains the address of the pointer.
```rust
let ptr: *const i32 = &42;
let usize_ptr = ptr as usize;
```
The `as usize` syntax will convert the pointer to a usize, which is an unsigned integer type that is the same size as a pointer. This allows you to store the address of the pointer in a usize, which can then be used for other operations.

## Helpful links
- [Rust Documentation - Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)
- [Rust Documentation - Primitive Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#primitive-types)
- [Rust Documentation - Casting](https://doc.rust-lang.org/book/ch03-02-data-types.html#casting)

group: rust-pointers