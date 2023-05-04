# Rust map example
// plain

A `map` in Rust is a collection of key-value pairs, where each key is unique. It is implemented as a `HashMap`, which is a hash table where the keys are hashed and stored in buckets.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();

map.insert("key1", "value1");
map.insert("key2", "value2");

println!("{:?}", map);
```

## Output example

```
{"key1": "value1", "key2": "value2"}
```

## Code explanation

- `use std::collections::HashMap;`: imports the `HashMap` type from the `std::collections` module.
- `let mut map = HashMap::new();`: creates a new empty `HashMap` and stores it in the `map` variable.
- `map.insert("key1", "value1");`: inserts a key-value pair into the `map`.
- `println!("{:?}", map);`: prints the contents of the `map` to the console.

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-map