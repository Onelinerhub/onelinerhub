# How to build a Rust HashMap from an iterator?
// plain

To build a Rust HashMap from an iterator, you can use the `collect()` method. This method takes an iterator and collects its elements into a collection. For example, the following code creates a HashMap from an iterator of tuples:

```rust
let map: HashMap<_, _> = [(1, "a"), (2, "b"), (3, "c")].iter().collect();
```

The output of this code is:

```
{1: "a", 2: "b", 3: "c"}
```

The code consists of the following parts:

- `let map: HashMap<_, _>`: This declares a variable `map` of type `HashMap` with generic type parameters `_` and `_`.
- `[(1, "a"), (2, "b"), (3, "c")]`: This is an array literal containing tuples of integers and strings.
- `.iter()`: This converts the array into an iterator.
- `.collect()`: This collects the elements of the iterator into a collection.

## Helpful links

- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Iterator documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-hashmap

onelinerhub: [How to build a Rust HashMap from an iterator?](https://onelinerhub.com/rust/how-to-build-a-rust-hashmap-from-an-iterator)