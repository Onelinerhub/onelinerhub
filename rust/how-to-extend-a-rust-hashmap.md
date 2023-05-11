# How to extend a Rust HashMap?
// plain

Extending a Rust HashMap is done by adding new key-value pairs to the existing map. This can be done using the `insert()` method.

```rust
use std::collections::HashMap;

let mut map = HashMap::new();

map.insert("key1", "value1");
map.insert("key2", "value2");
```

The code above creates a new HashMap and adds two key-value pairs to it.

- `let mut map = HashMap::new();` creates a new empty HashMap.
- `map.insert("key1", "value1");` adds a new key-value pair to the HashMap.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to extend a Rust HashMap?](https://onelinerhub.com/rust/how-to-extend-a-rust-hashmap)