# Pointer arithmetic example in Rust
// plain

Pointer arithmetic in Rust is a way of manipulating memory addresses. It is used to access data stored in memory, and can be used to iterate over collections of data. An example of pointer arithmetic in Rust is shown below:
```rust
let mut x = 5;
let mut y = &mut x;

y = y.offset(1);
```
This code snippet creates two variables, `x` and `y`, and assigns `x` the value of 5. `y` is then assigned the address of `x` using the `&mut` operator. Finally, `y` is incremented by one using the `offset` method.

The output of this code would be `6`, as `y` is now pointing to the memory address of `x` plus one.

The `&mut` operator is used to create a mutable reference to a variable, and the `offset` method is used to increment the memory address of a pointer. This allows us to manipulate memory addresses and access data stored in memory.

## Helpful links
- [Rust Pointer Arithmetic](https://doc.rust-lang.org/book/ch19-03-advanced-traits.html#using-the-offset-method-to-calculate-pointer-arithmetic)
- [Rust Mutable References](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html#mutable-references)
- [Rust Offset Method](https://doc.rust-lang.org/std/primitive.pointer.html#method.offset)

group: rust-pointers