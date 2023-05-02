# How to increment pointer in Rust
// plain

In Rust, you can increment a pointer by using the 'offset' method. This method takes an integer as an argument and adds that number to the pointer's address. For example, if you have a pointer to an integer, you can increment it by one with the following code:
```rust
let mut pointer = &mut 5;
pointer = pointer.offset(1);
```
The output of this code will be the address of the next integer in memory.

The offset method is useful for iterating through a collection of values. For example, if you have an array of integers, you can use the offset method to iterate through each element in the array:
```rust
let array = [1, 2, 3, 4, 5];
let mut pointer = &array[0];

for _ in 0..array.len() {
    println!("{}", *pointer);
    pointer = pointer.offset(1);
}
```
The output of this code will be the values of each element in the array.

## Helpful links
- [Rust Documentation - Pointer Arithmetic](https://doc.rust-lang.org/std/primitive.pointer.html#pointer-arithmetic)
- [Rust by Example - Pointers](https://doc.rust-lang.org/rust-by-example/scope/borrow/ref.html)
- [Rust Book - Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)

group: rust-pointers