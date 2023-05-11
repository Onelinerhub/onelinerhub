# How to convert a Rust slice to a tuple?
// plain

A Rust slice can be converted to a tuple by using the `.collect()` method. This method takes an iterator and collects its elements into a collection type.

```rust
let slice = [1, 2, 3];
let tuple: (i32, i32, i32) = slice.iter().collect();

println!("{:?}", tuple);
```

## Output example

```
(1, 2, 3)
```

The code above creates a slice of three elements and then uses the `.iter()` method to create an iterator over the slice. The `.collect()` method then collects the elements of the iterator into a tuple.

## Helpful links
- [Rust Documentation - Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)
- [Rust Documentation - Collect](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: rust-slice