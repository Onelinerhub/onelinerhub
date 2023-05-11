# How to convert a range to a vector in Rust?
// plain

To convert a range to a vector in Rust, you can use the `collect()` method. This method takes an iterator and collects its elements into a collection. For example:
```rust
let range = 0..10;
let vector: Vec<i32> = range.collect();
```
This will create a vector containing the numbers 0 to 10.

## Code explanation

- `let range = 0..10;`: This creates a range from 0 to 10.
- `let vector: Vec<i32> = range.collect();`: This collects the elements of the range into a vector.

## Helpful links
- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rust Documentation - Collect](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)