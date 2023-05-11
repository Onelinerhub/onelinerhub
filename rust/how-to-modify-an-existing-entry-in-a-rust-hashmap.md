# How to modify an existing entry in a Rust HashMap?
// plain

To modify an existing entry in a Rust HashMap, you can use the `insert()` method. This method takes two arguments, the key and the value, and replaces the existing value associated with the key with the new value.

## Example code

```
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key1", "value1");
map.insert("key1", "value2");
```

## Output example

```
()
```

## Code explanation

- `use std::collections::HashMap;`: imports the HashMap type from the standard library.
- `let mut map = HashMap::new();`: creates a new, empty HashMap.
- `map.insert("key1", "value1");`: inserts a new key-value pair into the HashMap.
- `map.insert("key1", "value2");`: replaces the existing value associated with the key "key1" with the new value "value2".

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to modify an existing entry in a Rust HashMap?](https://onelinerhub.com/rust/how-to-modify-an-existing-entry-in-a-rust-hashmap)