# How to add a value to a Rust HashMap?
// plain

Adding a value to a Rust HashMap is done using the `insert` method.

```rust
use std::collections::HashMap;

let mut map = HashMap::new();

map.insert("key", "value");
```

The code above creates a new `HashMap` and inserts a key-value pair into it. The `insert` method takes two arguments, the key and the value.

1. `use std::collections::HashMap`: imports the `HashMap` type from the `std::collections` module.
2. `let mut map = HashMap::new()`: creates a new `HashMap` and assigns it to the `map` variable.
3. `map.insert("key", "value")`: inserts a key-value pair into the `map` `HashMap`.

For more information, see the [Rust documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html).

group: rust-hashmap

onelinerhub: [How to add a value to a Rust HashMap?](https://onelinerhub.com/rust/how-to-add-a-value-to-a-rust-hashmap)