# How to convert the keys of a Rust HashMap to a HashSet?
// plain

To convert the keys of a Rust HashMap to a HashSet, you can use the `keys()` method of the HashMap. This will return an iterator of the keys in the HashMap. You can then use the `collect()` method to convert the iterator into a HashSet.

## Example code

```rust
use std::collections::{HashMap, HashSet};

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

let set: HashSet<&str> = map.keys().collect();
```

## Output example

```
{"a", "b", "c"}
```

## Code explanation


1. `let mut map = HashMap::new();` - This creates a new empty HashMap.
2. `map.insert("a", 1);` - This inserts a key-value pair into the HashMap.
3. `map.keys()` - This returns an iterator of the keys in the HashMap.
4. `collect()` - This method is used to convert the iterator into a HashSet.

## Helpful links

- [HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [HashSet documentation](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

group: rust-hashmap

onelinerhub: [How to convert the keys of a Rust HashMap to a HashSet?](https://onelinerhub.com/rust/how-to-convert-the-keys-of-a-rust-hashmap-to-a-hashset)