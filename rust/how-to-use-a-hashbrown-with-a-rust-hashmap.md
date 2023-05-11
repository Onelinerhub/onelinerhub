# How to use a HashBrown with a Rust HashMap?
// plain

Using a `HashBrown` with a `HashMap` in Rust is easy.

```rust
use std::collections::HashMap;
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

let mut map = HashMap::new();
let mut hasher = DefaultHasher::new();

// Insert a key-value pair into the map
map.insert("key", "value");

// Hash the key
"key".hash(&mut hasher);

// Get the hashed key
let hashed_key = hasher.finish();

// Get the value associated with the hashed key
let value = map.get(&hashed_key);

println!("{:?}", value);
```

## Output example

```
Some("value")
```

The code above demonstrates how to use a `HashBrown` with a `HashMap` in Rust. First, we create a `HashMap` and a `DefaultHasher`. Then, we insert a key-value pair into the map. Next, we hash the key using the `hash` method. Finally, we get the hashed key and the value associated with it.

- `use std::collections::HashMap`: imports the `HashMap` type from the `std::collections` module.
- `use std::collections::hash_map::DefaultHasher`: imports the `DefaultHasher` type from the `std::collections::hash_map` module.
- `use std::hash::{Hash, Hasher}`: imports the `Hash` and `Hasher` traits from the `std::hash` module.
- `let mut map = HashMap::new()`: creates a new `HashMap`.
- `let mut hasher = DefaultHasher::new()`: creates a new `DefaultHasher`.
- `map.insert("key", "value")`: inserts a key-value pair into the map.
- `"key".hash(&mut hasher)`: hashes the key using the `hash` method.
- `let hashed_key = hasher.finish()`: gets the hashed key.
- `let value = map.get(&hashed_key)`: gets the value associated with the hashed key.
- `println!("{:?}", value)`: prints the value.

## Helpful links
- [HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Hash Documentation](https://doc.rust-lang.org/std/hash/trait.Hash.html)
- [Hasher Documentation](https://doc.rust-lang.org/std/hash/trait.Hasher.html)

group: rust-hashmap

onelinerhub: [How to use a HashBrown with a Rust HashMap?](https://onelinerhub.com/rust/how-to-use-a-hashbrown-with-a-rust-hashmap)