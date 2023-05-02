# How to iterate over pointer in Rust
// plain

To iterate over a pointer in Rust, you can use the `.iter()` method. This method returns an iterator over the pointer's elements. For example, if you have a pointer to an array of integers, you can use the `.iter()` method to iterate over the array:
```rust
let arr = [1, 2, 3];
let ptr = &arr;

for x in ptr.iter() {
    println!("{}", x);
}
```
This code will print out each element of the array, one per line. The `.iter()` method returns an iterator, which is a type of object that can be used to iterate over a collection of elements. The iterator will return each element of the array in turn, allowing you to process each element in the loop.

In addition to `.iter()`, Rust also provides the `.iter_mut()` method, which returns an iterator over mutable references to the pointer's elements. This can be used to modify the elements of the pointer in a loop.

## Helpful links
- [Rust Documentation - Iterators](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rust Documentation - Pointers](https://doc.rust-lang.org/book/ch19-01-pointers.html)
- [Rust Documentation - Iterator Trait](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-pointers