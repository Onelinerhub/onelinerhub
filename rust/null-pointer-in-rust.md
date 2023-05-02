# Null pointer in Rust
// plain

.

A null pointer in Rust is a pointer that does not point to any valid object. It is represented by the type `std::ptr::null()`. This type is used to indicate that a pointer is not pointing to a valid object. For example, the following code creates a null pointer and prints its value:
```rust
let ptr: *const i32 = std::ptr::null();
println!("{:?}", ptr);
```
The output of this code is `0x0`, which indicates that the pointer is not pointing to a valid object.

Null pointers can be used to indicate an error condition or to indicate that a pointer is not pointing to a valid object. For example, the following code checks if a pointer is null and prints an error message if it is:
```rust
let ptr: *const i32 = std::ptr::null();
if ptr.is_null() {
    println!("Error: pointer is null!");
}
```

## Helpful links
- [Rust Documentation - Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)
- [Rust Documentation - std::ptr](https://doc.rust-lang.org/std/ptr/)
- [Rust by Example - Pointers](https://doc.rust-lang.org/rust-by-example/std_misc/pointers.html)

group: rust-pointers