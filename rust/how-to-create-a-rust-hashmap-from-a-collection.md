# How to create a Rust HashMap from a collection?
// plain

Creating a Rust HashMap from a collection is a simple process. First, create a vector of tuples containing the key and value. Then, use the `collect()` method to convert the vector into a HashMap.

```rust
let mut map = vec![("a", 1), ("b", 2), ("c", 3)].into_iter().collect::<HashMap<_, _>>();
```

The output of the above code is a HashMap with the keys `a`, `b`, and `c` and the corresponding values `1`, `2`, and `3`:

```
{"a": 1, "b": 2, "c": 3}
```

The code consists of the following parts:

- `vec![("a", 1), ("b", 2), ("c", 3)]`: This creates a vector of tuples containing the keys and values.
- `into_iter()`: This converts the vector into an iterator.
- `collect::<HashMap<_, _>>()`: This collects the iterator into a HashMap.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Collect Documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)

group: rust-hashmap

onelinerhub: [How to create a Rust HashMap from a collection?](https://onelinerhub.com/rust/how-to-create-a-rust-hashmap-from-a-collection)