# How to access a mutable index in a Rust HashMap?
// plain

Accessing a mutable index in a Rust HashMap can be done using the `entry` method. This method returns a mutable reference to the corresponding value in the HashMap.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key", "value");

let entry = map.entry("key").or_insert("new value");
*entry = "updated value";

println!("{:?}", map);
```

## Output example

```
{"key": "updated value"}
```

## Code explanation


1. `let mut map = HashMap::new();` - creates a new empty HashMap.
2. `map.insert("key", "value");` - inserts a key-value pair into the HashMap.
3. `let entry = map.entry("key").or_insert("new value");` - returns a mutable reference to the corresponding value in the HashMap. If the key does not exist, a new key-value pair is inserted with the given value.
4. `*entry = "updated value";` - updates the value of the key-value pair.
5. `println!("{:?}", map);` - prints the HashMap.

## Helpful links

- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to access a mutable index in a Rust HashMap?](https://onelinerhub.com/rust/how-to-access-a-mutable-index-in-a-rust-hashmap)