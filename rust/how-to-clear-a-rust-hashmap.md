# How to clear a Rust HashMap?
// plain

To clear a Rust `HashMap`, use the `clear()` method. This method will remove all elements from the `HashMap`.

## Example

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);

map.clear();

assert!(map.is_empty());
```

## Output example

```
```

The `clear()` method takes no arguments and returns nothing. It simply removes all elements from the `HashMap`.

## Helpful links

- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to clear a Rust HashMap?](https://onelinerhub.com/rust/how-to-clear-a-rust-hashmap)