# How to create a Rust HashMap?
// plain

Creating a Rust HashMap is easy and straightforward.

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key1", "value1");
map.insert("key2", "value2");
```

The output of the above code will be:
```
()
```

## Code explanation

1. `use std::collections::HashMap;` - This imports the HashMap module from the standard library.
2. `let mut map = HashMap::new();` - This creates a new, empty HashMap.
3. `map.insert("key1", "value1");` - This inserts a key-value pair into the HashMap.
4. `map.insert("key2", "value2");` - This inserts another key-value pair into the HashMap.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to create a Rust HashMap?](https://onelinerhub.com/rust/how-to-create-a-rust-hashmap)