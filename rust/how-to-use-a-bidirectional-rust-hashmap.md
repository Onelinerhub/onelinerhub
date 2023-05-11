# How to use a bidirectional Rust HashMap?
// plain

A bidirectional Rust HashMap is a data structure that allows for efficient lookup of keys and values. It is implemented using a hash table, which allows for fast lookups and insertion of elements.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();

map.insert("foo", "bar");
map.insert("baz", "qux");

let value = map.get("foo");
println!("{:?}", value);
```

## Output example

```
Some("bar")
```

## Code explanation


1. `use std::collections::HashMap;`: This imports the HashMap type from the standard library.

2. `let mut map = HashMap::new();`: This creates a new, empty HashMap.

3. `map.insert("foo", "bar");`: This inserts a key-value pair into the HashMap.

4. `let value = map.get("foo");`: This retrieves the value associated with the given key from the HashMap.

5. `println!("{:?}", value);`: This prints the retrieved value to the console.

## Helpful links

- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to use a bidirectional Rust HashMap?](https://onelinerhub.com/rust/how-to-use-a-bidirectional-rust-hashmap)