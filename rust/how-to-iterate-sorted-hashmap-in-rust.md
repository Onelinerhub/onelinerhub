# How to iterate sorted hashmap in Rust
// plain

Iterating over a sorted hashmap in Rust can be done using the `iter()` method. This method returns an iterator over the key-value pairs in the map, in ascending order by key.

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

- `use std::collections::HashMap`: imports the `HashMap` type from the `std::collections` module.
- `let mut map = HashMap::new()`: creates a new, empty `HashMap` instance.
- `map.insert("a", 1)`: inserts a key-value pair into the `HashMap`.
- `for (key, value) in map.iter()`: iterates over the key-value pairs in the `HashMap`, in ascending order by key.
- `println!("{}: {}", key, value)`: prints the key and value of the current iteration.

## Helpful links
- [HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-loops