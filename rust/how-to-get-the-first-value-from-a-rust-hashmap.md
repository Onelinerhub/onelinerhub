# How to get the first value from a Rust HashMap?
// plain

The first value from a Rust HashMap can be obtained using the `get` method. This method takes a reference to the key and returns an `Option<&V>` where `V` is the type of the value associated with the key.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key1", "value1");
map.insert("key2", "value2");

let first_value = map.get("key1");
```

## Output example

```
Some("value1")
```

## Code explanation

- `use std::collections::HashMap`: imports the `HashMap` type from the `std::collections` module.
- `let mut map = HashMap::new()`: creates a new empty `HashMap` instance.
- `map.insert("key1", "value1")`: inserts a key-value pair into the `HashMap`.
- `let first_value = map.get("key1")`: gets the value associated with the key `"key1"` from the `HashMap`.

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to get the first value from a Rust HashMap?](https://onelinerhub.com/rust/how-to-get-the-first-value-from-a-rust-hashmap)