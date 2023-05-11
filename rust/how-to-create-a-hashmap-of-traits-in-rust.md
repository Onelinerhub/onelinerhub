# How to create a HashMap of traits in Rust?
// plain

A HashMap is a data structure in Rust that stores key-value pairs. It is a collection of unique keys and their associated values. To create a HashMap of traits, you can use the `HashMap::new()` method.

```rust
use std::collections::HashMap;

let mut traits = HashMap::new();

traits.insert("strength", 10);
traits.insert("intelligence", 8);
traits.insert("charisma", 5);
```

The output of the example code is:
```
()
```

## Code explanation


1. `use std::collections::HashMap;` - This imports the HashMap module from the standard library.

2. `let mut traits = HashMap::new();` - This creates a new, empty HashMap called `traits`.

3. `traits.insert("strength", 10);` - This inserts a key-value pair into the HashMap, with the key being "strength" and the value being 10.

4. `traits.insert("intelligence", 8);` - This inserts a key-value pair into the HashMap, with the key being "intelligence" and the value being 8.

5. `traits.insert("charisma", 5);` - This inserts a key-value pair into the HashMap, with the key being "charisma" and the value being 5.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to create a HashMap of traits in Rust?](https://onelinerhub.com/rust/how-to-create-a-hashmap-of-traits-in-rust)