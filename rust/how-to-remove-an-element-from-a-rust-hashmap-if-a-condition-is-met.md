# How to remove an element from a Rust HashMap if a condition is met?
// plain

Removing an element from a Rust HashMap if a condition is met can be done using the `remove_entry` method. This method takes a closure as an argument, which is used to determine if the element should be removed.

## Example code

```rust
let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

map.remove_entry(|key, value| *value == 2);
```

## Output example

```
()
```

## Code explanation

- `let mut map = HashMap::new();`: creates a new empty HashMap
- `map.insert("a", 1);`: inserts a key-value pair into the HashMap
- `map.remove_entry(|key, value| *value == 2);`: removes an entry from the HashMap if the closure returns true

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to remove an element from a Rust HashMap if a condition is met?](https://onelinerhub.com/rust/how-to-remove-an-element-from-a-rust-hashmap-if-a-condition-is-met)