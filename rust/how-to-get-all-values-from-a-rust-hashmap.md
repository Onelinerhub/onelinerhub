# How to get all values from a Rust HashMap?
// plain

You can get all values from a Rust HashMap using the `values()` method. This method returns an iterator over the values of the HashMap.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

for value in map.values() {
    println!("{}", value);
}
```

## Output example

```
1
2
3
```

## Code explanation

- `use std::collections::HashMap`: imports the HashMap type from the standard library.
- `let mut map = HashMap::new()`: creates a new empty HashMap.
- `map.insert("a", 1)`: inserts a key-value pair into the HashMap.
- `for value in map.values()`: iterates over the values of the HashMap.
- `println!("{}", value)`: prints the value to the console.

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to get all values from a Rust HashMap?](https://onelinerhub.com/rust/how-to-get-all-values-from-a-rust-hashmap)