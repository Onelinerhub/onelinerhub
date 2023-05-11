# How to create a nested HashMap in Rust?
// plain

Nested HashMap in Rust can be created using the `HashMap::new()` method. The following example code creates a nested HashMap with two levels of nesting:

```rust
use std::collections::HashMap;

let mut map = HashMap::new();

let mut inner_map = HashMap::new();
inner_map.insert("key1", "value1");
inner_map.insert("key2", "value2");

map.insert("inner_map", inner_map);

println!("{:?}", map);
```

## Output example

```
{"inner_map": {"key1": "value1", "key2": "value2"}}
```

## Code explanation

1. `use std::collections::HashMap;` - imports the `HashMap` type from the `std::collections` module.
2. `let mut map = HashMap::new();` - creates a new empty `HashMap` and stores it in the `map` variable.
3. `let mut inner_map = HashMap::new();` - creates a new empty `HashMap` and stores it in the `inner_map` variable.
4. `inner_map.insert("key1", "value1");` - inserts a key-value pair into the `inner_map` `HashMap`.
5. `map.insert("inner_map", inner_map);` - inserts the `inner_map` `HashMap` into the `map` `HashMap`.
6. `println!("{:?}", map);` - prints the contents of the `map` `HashMap`.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to create a nested HashMap in Rust?](https://onelinerhub.com/rust/how-to-create-a-nested-hashmap-in-rust)