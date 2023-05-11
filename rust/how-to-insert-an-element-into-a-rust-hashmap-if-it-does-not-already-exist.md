# How to insert an element into a Rust HashMap if it does not already exist?
// plain

To insert an element into a Rust HashMap if it does not already exist, the `entry` API can be used. This API takes a key and a closure as arguments. The closure is called with a mutable reference to the value corresponding to the key, if it exists. The closure can then be used to insert the element if it does not already exist.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();

map.entry("key").or_insert("value");
```

## Output example

```
()
```

## Code explanation

- `entry`: API used to insert an element into a Rust HashMap if it does not already exist.
- `key`: Key of the element to be inserted.
- `or_insert`: Closure called with a mutable reference to the value corresponding to the key, if it exists.

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to insert an element into a Rust HashMap if it does not already exist?](https://onelinerhub.com/rust/how-to-insert-an-element-into-a-rust-hashmap-if-it-does-not-already-exist)