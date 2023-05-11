# How to get a reference to a key in a Rust HashMap?
// plain

You can get a reference to a key in a Rust HashMap using the `get` method. This method returns an `Option<&V>` where `V` is the type of the value associated with the key.

## Example

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key1", "value1");
map.insert("key2", "value2");

let value = map.get("key1");
println!("{:?}", value);
```
## Output example

```
Some("value1")
```

The `get` method takes a reference to the key and returns an `Option` type. If the key is present in the HashMap, the `Option` will contain a reference to the value associated with the key. If the key is not present, the `Option` will be `None`.

## Code explanation

- `get` method: takes a reference to the key and returns an `Option` type
- `Option` type: if the key is present, contains a reference to the value associated with the key; if the key is not present, is `None`

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to get a reference to a key in a Rust HashMap?](https://onelinerhub.com/rust/how-to-get-a-reference-to-a-key-in-a-rust-hashmap)