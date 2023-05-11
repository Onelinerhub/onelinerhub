# How to implement a HashMap in Rust?
// plain

A HashMap in Rust can be implemented using the `HashMap` type from the `std::collections` module.

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

The code above creates a new `HashMap` and inserts two key-value pairs into it. The `insert` method takes two parameters, the key and the value, and adds them to the map. The `println!` macro prints the contents of the map.

Parts of the code:
- `use std::collections::HashMap;`: imports the `HashMap` type from the `std::collections` module.
- `let mut map = HashMap::new();`: creates a new `HashMap` and assigns it to the `map` variable.
- `map.insert("key1", "value1");`: inserts a key-value pair into the map.
- `println!("{:?}", map);`: prints the contents of the map.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to implement a HashMap in Rust?](https://onelinerhub.com/rust/how-to-implement-a-hashmap-in-rust)