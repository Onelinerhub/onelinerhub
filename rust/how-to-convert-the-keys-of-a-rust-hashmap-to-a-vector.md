# How to convert the keys of a Rust HashMap to a vector?
// plain

To convert the keys of a Rust HashMap to a vector, you can use the `keys()` method. This will return an iterator over the keys of the HashMap. You can then use the `collect()` method to convert the iterator into a vector.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

let keys: Vec<&str> = map.keys().collect();

println!("{:?}", keys);
```

## Output example

```
["a", "b", "c"]
```

## Code explanation

- `let mut map = HashMap::new();`: This creates a new empty HashMap.
- `map.insert("a", 1);`: This inserts a key-value pair into the HashMap.
- `let keys: Vec<&str> = map.keys().collect();`: This uses the `keys()` method to get an iterator over the keys of the HashMap, and then uses the `collect()` method to convert the iterator into a vector.
- `println!("{:?}", keys);`: This prints the vector of keys.

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Iterator documentation](https://doc.rust-lang.org/std/iter/trait.Iterator.html)

group: rust-hashmap

onelinerhub: [How to convert the keys of a Rust HashMap to a vector?](https://onelinerhub.com/rust/how-to-convert-the-keys-of-a-rust-hashmap-to-a-vector)