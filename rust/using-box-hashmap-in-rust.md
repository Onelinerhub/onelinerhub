# Using box hashmap in Rust
// plain

Box hashmap is a type of hashmap in Rust that allows for the storage of values on the heap. It is similar to a regular hashmap, but it is more efficient in terms of memory usage.

Example code:
```
use std::collections::HashMap;

let mut map = Box::new(HashMap::new());
map.insert("key", "value");
```

Output:
```
()
```

Code parts with detailed explanation:
- `use std::collections::HashMap;`: This imports the HashMap type from the standard library.
- `let mut map = Box::new(HashMap::new());`: This creates a new Box hashmap and assigns it to the variable `map`.
- `map.insert("key", "value");`: This inserts a key-value pair into the hashmap.

## Helpful links
- [Rust Documentation - Box](https://doc.rust-lang.org/std/boxed/struct.Box.html)
- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-box