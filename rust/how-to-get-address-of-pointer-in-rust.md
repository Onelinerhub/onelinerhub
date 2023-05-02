# How to get address of pointer in Rust
// plain

In Rust, you can get the address of a pointer by using the `&` operator. For example, if you have a pointer `ptr` pointing to a value `val`, you can get the address of `ptr` by using `&ptr`. The ## Code example below shows how to get the address of a pointer:
```rust
let val = 10;
let ptr = &val;
let address = &ptr;
println!("The address of the pointer is {:p}", address);
```
The output of the code above will be:
```
The address of the pointer is 0x7ffc9f9f9f90
```
The `&` operator is used to get the address of a pointer. In this example, `ptr` is a pointer pointing to the value `val`, and `address` is a pointer pointing to the address of `ptr`. The `println!` macro is used to print the address of `ptr` to the console. The `{:p}` format specifier is used to print the address in a hexadecimal format.

## Helpful links
- [Rust Reference - Pointers](https://doc.rust-lang.org/reference/pointers.html)
- [Rust Reference - Formatting](https://doc.rust-lang.org/reference/formatting.html)
- [Rust Reference - Macros](https://doc.rust-lang.org/reference/macros.html)

group: rust-pointers