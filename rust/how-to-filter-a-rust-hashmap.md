# How to filter a Rust HashMap?
// plain

Filtering a Rust HashMap can be done using the `filter` method. This method takes a closure as an argument and returns a new HashMap with only the elements that satisfy the closure.

## Example code

```rust
let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

let filtered_map = map.filter(|&(_, v)| v > 1);
```

## Output example

```
{"b": 2, "c": 3}
```

## Code explanation

- `let mut map = HashMap::new();`: creates a new empty HashMap
- `map.insert("a", 1);`: inserts a key-value pair into the HashMap
- `map.insert("b", 2);`: inserts a key-value pair into the HashMap
- `map.insert("c", 3);`: inserts a key-value pair into the HashMap
- `let filtered_map = map.filter(|&(_, v)| v > 1);`: filters the HashMap using the `filter` method, which takes a closure as an argument and returns a new HashMap with only the elements that satisfy the closure

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to filter a Rust HashMap?](https://onelinerhub.com/rust/how-to-filter-a-rust-hashmap)