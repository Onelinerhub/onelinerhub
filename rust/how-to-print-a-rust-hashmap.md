# How to print a Rust HashMap?
// plain

Printing a Rust HashMap is easy and can be done in a few steps.

## Example code

```
use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert("key1", "value1");
    map.insert("key2", "value2");

    for (key, value) in &map {
        println!("{}: {}", key, value);
    }
}
```

## Output example

```
key1: value1
key2: value2
```

The code consists of the following parts:
1. `use std::collections::HashMap;` - imports the HashMap type from the standard library.
2. `let mut map = HashMap::new();` - creates a new empty HashMap.
3. `map.insert("key1", "value1");` - inserts a key-value pair into the HashMap.
4. `map.insert("key2", "value2");` - inserts another key-value pair into the HashMap.
5. `for (key, value) in &map {` - iterates over the HashMap.
6. `println!("{}: {}", key, value);` - prints the key-value pair.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to print a Rust HashMap?](https://onelinerhub.com/rust/how-to-print-a-rust-hashmap)