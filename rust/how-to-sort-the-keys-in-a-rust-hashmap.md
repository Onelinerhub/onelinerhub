# How to sort the keys in a Rust HashMap?
// plain

Rust HashMap can be sorted by its keys using the `.iter()` method. This method returns an iterator over the key-value pairs in the map, sorted by the keys.

## Example code

```
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

for (key, value) in map.iter() {
    println!("{}: {}", key, value);
}
```

## Output example

```
a: 1
b: 2
c: 3
```

## Code explanation

- `use std::collections::HashMap;`: imports the HashMap type from the standard library.
- `let mut map = HashMap::new();`: creates a new empty HashMap.
- `map.insert("a", 1);`: inserts a key-value pair into the HashMap.
- `for (key, value) in map.iter() {`: iterates over the key-value pairs in the map, sorted by the keys.
- `println!("{}: {}", key, value);`: prints the key-value pair.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to sort the keys in a Rust HashMap?](https://onelinerhub.com/rust/how-to-sort-the-keys-in-a-rust-hashmap)