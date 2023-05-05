# How do you map strings in Rust?
// plain

Strings in Rust are mapped using the `HashMap` type, which is a part of the standard library. `HashMap` is a key-value store that allows you to store data using a key and retrieve it using the same key.

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

- `use std::collections::HashMap;`: imports the `HashMap` type from the standard library.
- `let mut map = HashMap::new();`: creates a new `HashMap` instance.
- `map.insert("key1", "value1");`: inserts a key-value pair into the `HashMap`.
- `println!("{:?}", map);`: prints the contents of the `HashMap`.

## Helpful links
- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)