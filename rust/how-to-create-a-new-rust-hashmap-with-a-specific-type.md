# How to create a new Rust HashMap with a specific type?
// plain

Creating a new Rust HashMap with a specific type is easy. You can use the `HashMap::new` method to create a new empty HashMap. The type of the HashMap is specified by the type of the key and value.

## Example code

```rust
use std::collections::HashMap;

let mut map: HashMap<String, i32> = HashMap::new();
```

This example creates a new empty HashMap with `String` as the key type and `i32` as the value type.

## Code explanation

- `use std::collections::HashMap;`: imports the `HashMap` type from the `std::collections` module.
- `let mut map: HashMap<String, i32> = HashMap::new();`: creates a new empty HashMap with `String` as the key type and `i32` as the value type.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to create a new Rust HashMap with a specific type?](https://onelinerhub.com/rust/how-to-create-a-new-rust-hashmap-with-a-specific-type)