# How to create a new Rust HashMap with values?
// plain

Creating a new Rust HashMap with values is easy. You can use the `collect()` method to create a HashMap from a vector of key-value pairs.

```rust
let mut map = vec![("a", 1), ("b", 2), ("c", 3)].into_iter().collect::<HashMap<_, _>>();
```

This code creates a HashMap with the keys `"a"`, `"b"`, and `"c"` and the corresponding values `1`, `2`, and `3`.

The code consists of the following parts:

1. `let mut map =`: This declares a mutable variable `map` to store the HashMap.
2. `vec![("a", 1), ("b", 2), ("c", 3)]`: This creates a vector of key-value pairs.
3. `.into_iter()`: This converts the vector into an iterator.
4. `.collect::<HashMap<_, _>>()`: This collects the iterator into a HashMap.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Collect Method Documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: rust-hashmap

onelinerhub: [How to create a new Rust HashMap with values?](https://onelinerhub.com/rust/how-to-create-a-new-rust-hashmap-with-values)