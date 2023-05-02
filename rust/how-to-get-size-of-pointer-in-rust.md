# How to get size of pointer in Rust
// plain

The size of a pointer in Rust depends on the platform it is running on. Generally, a pointer in Rust is the same size as a usize, which is typically 8 bytes on 64-bit platforms and 4 bytes on 32-bit platforms. To get the size of a pointer in Rust, you can use the std::mem::size_of function. For example:
```
let size = std::mem::size_of::<*const i32>();
```
This code will return the size of a pointer to an i32 in bytes. The output of this code will be 8 on a 64-bit platform and 4 on a 32-bit platform.

In addition to the size_of function, Rust also provides the size_of_val function, which can be used to get the size of a value. For example:
```
let size = std::mem::size_of_val(&42);
```
This code will return the size of the value 42 in bytes. The output of this code will be 4 on both 32-bit and 64-bit platforms.

## Helpful links
- [std::mem::size_of](https://doc.rust-lang.org/std/mem/fn.size_of.html)
- [std::mem::size_of_val](https://doc.rust-lang.org/std/mem/fn.size_of_val.html)
- [Rust Platforms](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#platform-specific-size-and-alignment)

group: rust-pointers