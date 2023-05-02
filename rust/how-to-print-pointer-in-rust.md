# How to print pointer in Rust
// plain

In Rust, you can print a pointer by using the `std::ptr::Pointer` trait. To do this, you must first create a pointer to the data you want to print. Then, you can use the `std::fmt::Pointer` trait to print the pointer. For example:
```rust
let data = 10;
let ptr = &data;
println!("{:p}", ptr);
```
This will print the pointer to the data, which will look something like `0x7ffc9f9f9f90`.

The `std::fmt::Pointer` trait also allows you to customize the output of the pointer. For example, you can specify the base of the pointer (hexadecimal, octal, etc.) and the width of the pointer. For more information, see the [Rust documentation](https://doc.rust-lang.org/std/fmt/trait.Pointer.html).

## Helpful links
- [Rust documentation - Pointer trait](https://doc.rust-lang.org/std/fmt/trait.Pointer.html)
- [Rust by Example - Pointers](https://doc.rust-lang.org/rust-by-example/scope/borrow/ref.html)
- [Rust Book - Pointers and References](https://doc.rust-lang.org/book/ch15-01-box.html)

group: rust-pointers