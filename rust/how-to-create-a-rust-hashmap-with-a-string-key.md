# How to create a Rust HashMap with a string key?
// plain

Creating a Rust HashMap with a string key is easy. The following example code creates a HashMap with a string key and a value of type i32:

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("key", 42);
```

The output of the code is:

```
()
```

The code consists of the following parts:

1. `use std::collections::HashMap;` - imports the HashMap type from the standard library.
2. `let mut map = HashMap::new();` - creates a new empty HashMap.
3. `map.insert("key", 42);` - inserts a key-value pair into the HashMap.

For more information, see the [Rust documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html).

group: rust-hashmap

onelinerhub: [How to create a Rust HashMap with a string key?](https://onelinerhub.com/rust/how-to-create-a-rust-hashmap-with-a-string-key)