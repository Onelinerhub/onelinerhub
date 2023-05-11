# How to get the length of a Rust HashMap?
// plain

The length of a Rust HashMap can be obtained using the `len()` method.

## Example code

```
use std::collections::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);

println!("Length of map: {}", map.len());
```

## Output example

```
Length of map: 2
```

## Code explanation


1. `use std::collections::HashMap;` - imports the `HashMap` type from the `std::collections` module.
2. `let mut map = HashMap::new();` - creates a new empty `HashMap` instance.
3. `map.insert("a", 1);` - inserts a key-value pair into the `HashMap`.
4. `map.insert("b", 2);` - inserts another key-value pair into the `HashMap`.
5. `println!("Length of map: {}", map.len());` - prints the length of the `HashMap` to the console.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to get the length of a Rust HashMap?](https://onelinerhub.com/rust/how-to-get-the-length-of-a-rust-hashmap)