# How to iterate btreemap in Rust
// plain

Iterating over a `BTreeMap` in Rust can be done using the `iter()` method. This method returns an iterator over the entries of the map, which can then be used to access the key-value pairs.

## Example code

```rust
use std::collections::BTreeMap;

let mut map = BTreeMap::new();
map.insert("a", 1);
map.insert("b", 2);

for (key, value) in map.iter() {
    println!("key: {} value: {}", key, value);
}
```

## Output example

```
key: a value: 1
key: b value: 2
```

## Code explanation

- `use std::collections::BTreeMap;`: imports the `BTreeMap` type from the `std::collections` module.
- `let mut map = BTreeMap::new();`: creates a new empty `BTreeMap`.
- `map.insert("a", 1);`: inserts a key-value pair into the `BTreeMap`.
- `for (key, value) in map.iter() {`: starts an iterator loop over the entries of the `BTreeMap`.
- `println!("key: {} value: {}", key, value);`: prints the key and value of the current entry.

## Helpful links
- [Rust Documentation - BTreeMap](https://doc.rust-lang.org/std/collections/struct.BTreeMap.html)

group: rust-loops