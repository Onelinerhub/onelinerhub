# How to get all keys from a Rust HashMap?
// plain

You can get all keys from a Rust HashMap using the `keys()` method. This method returns an iterator over the keys of the map.

## Example code

```rust
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);

for key in map.keys() {
    println!("{}", key);
}
```

## Output example

```
a
b
```

## Code explanation

- `use std::collections::HashMap`: imports the `HashMap` type from the `std::collections` module.
- `let mut map = HashMap::new()`: creates a new empty `HashMap` and stores it in the `map` variable.
- `map.insert("a", 1)`: inserts a key-value pair into the `map` variable.
- `map.keys()`: returns an iterator over the keys of the `map` variable.
- `for key in map.keys()`: iterates over the keys of the `map` variable.
- `println!("{}", key)`: prints the current key to the console.

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to get all keys from a Rust HashMap?](https://onelinerhub.com/rust/how-to-get-all-keys-from-a-rust-hashmap)