# How to delete pointer in Rust
// plain

In Rust, you can delete a pointer by using the `std::mem::drop` function. This function takes a mutable reference to the pointer and deallocates the memory associated with it. To use this function, you must first create a mutable reference to the pointer using the `&mut` operator. Then, you can call the `drop` function on the reference. For example:
```rust
let mut ptr = Box::new(5);
drop(&mut ptr);
```
This code creates a pointer to an integer with the value 5, and then calls the `drop` function on the pointer. This deallocates the memory associated with the pointer, effectively deleting it.

It is important to note that the `drop` function does not set the pointer to `null`. If you try to access the pointer after calling `drop`, you will get an error. To avoid this, you should set the pointer to `null` after calling `drop`. For example:
```rust
let mut ptr = Box::new(5);
drop(&mut ptr);
ptr = null;
```
This code calls the `drop` function on the pointer, and then sets the pointer to `null`. This ensures that the pointer is no longer valid and cannot be accessed.

## Helpful links
- [std::mem::drop](https://doc.rust-lang.org/std/mem/fn.drop.html)
- [Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [null](https://doc.rust-lang.org/std/ptr/fn.null.html)

group: rust-pointers