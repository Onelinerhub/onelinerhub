# How to check if a Rust HashMap contains a key?
// plain

To check if a Rust HashMap contains a key, you can use the `contains_key` method. This method takes a reference to the key as an argument and returns a boolean value indicating whether the key is present in the HashMap or not.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key1", "value1");

if map.contains_key("key1") {
    println!("key1 is present in the HashMap");
}
```

## Output example

```
key1 is present in the HashMap
```

## Code explanation

- `use std::collections::HashMap`: imports the HashMap type from the standard library.
- `let mut map = HashMap::new()`: creates a new empty HashMap.
- `map.insert("key1", "value1")`: inserts a key-value pair into the HashMap.
- `if map.contains_key("key1")`: checks if the HashMap contains the specified key.
- `println!("key1 is present in the HashMap")`: prints a message if the key is present in the HashMap.

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to check if a Rust HashMap contains a key?](https://onelinerhub.com/rust/how-to-check-if-a-rust-hashmap-contains-a-key)