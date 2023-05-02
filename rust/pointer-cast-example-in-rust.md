# Pointer cast example in Rust
// plain

Pointer casting in Rust is a way to convert a pointer of one type to a pointer of another type. This is done by using the `as` keyword. For example, to convert a pointer of type `*const i32` to a pointer of type `*mut i32`, you can use the following code:
```rust
let ptr_const: *const i32 = &42;
let ptr_mut: *mut i32 = ptr_const as *mut i32;
```
### Output example
No output example
### Explanation
The `as` keyword is used to cast the pointer `ptr_const` of type `*const i32` to a pointer of type `*mut i32`. This is done by assigning the result of the cast to the variable `ptr_mut`.
### Relevant links
[Rust Pointer Casting](https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html#dereferencing-a-raw-pointer)
[Rust Pointer Types](https://doc.rust-lang.org/book/ch19-02-advanced-features.html#pointer-types)
[Rust Pointer Safety](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#pointer-safety)

group: rust-pointers