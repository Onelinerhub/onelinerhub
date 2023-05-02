# Creating pointer from specific address in Rust
// plain

In Rust, you can create a pointer from a specific address using the `std::ptr::NonNull` type. This type is a wrapper around a raw pointer that ensures that the pointer is not null. To create a pointer from a specific address, you can use the `new_unchecked` method, which takes a raw pointer and returns a `NonNull` instance. For example, to create a pointer from the address `0x12345678`, you can use the following code:

```rust
let ptr = std::ptr::NonNull::new_unchecked(0x12345678 as *mut i32);
```

The `new_unchecked` method does not perform any checks on the pointer, so it is important to make sure that the pointer is valid before using it. If the pointer is invalid, it can lead to undefined behavior.

## Helpful links
- [std::ptr::NonNull](https://doc.rust-lang.org/std/ptr/struct.NonNull.html)
- [Raw Pointers](https://doc.rust-lang.org/book/ch19-01-unsafe-rust.html#dereferencing-raw-pointers)
- [Undefined Behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html)

group: rust-pointers