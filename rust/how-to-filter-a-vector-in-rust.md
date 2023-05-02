# How to filter a vector in Rust
// plain

To filter a vector in Rust, you can use the `filter()` method. This method takes a closure as an argument and returns a new vector with only the elements that satisfy the closure's condition. For example, to filter a vector of numbers and keep only the even numbers:
```rust
let numbers = vec![1, 2, 3, 4, 5];
let even_numbers: Vec<i32> = numbers.into_iter().filter(|x| x % 2 == 0).collect();
// even_numbers is now [2, 4]
```
The `filter()` method iterates over the vector and applies the closure to each element. If the closure returns `true`, the element is kept in the new vector, otherwise it is discarded. In the example above, the closure checks if the number is even and returns `true` if it is.

## Helpful links
- [Rust Documentation - Iterator::filter](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.filter)
- [Rust by Example - Iterators](https://doc.rust-lang.org/rust-by-example/iter.html)
- [Rust Cookbook - Filter a Vector](https://rust-lang-nursery.github.io/rust-cookbook/algorithms/filtering.html)