# How to map values in a Rust HashMap?
// plain

Mapping values in a Rust HashMap is done using the `insert` method. This method takes two arguments, a key and a value, and adds them to the HashMap.

## Example

```
let mut map = HashMap::new();
map.insert("key1", "value1");
map.insert("key2", "value2");
```

## Output example

```
()
```

## Code explanation

- `let mut map = HashMap::new();`: creates a new, empty HashMap
- `map.insert("key1", "value1");`: inserts a key-value pair into the HashMap
- `map.insert("key2", "value2");`: inserts another key-value pair into the HashMap

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to map values in a Rust HashMap?](https://onelinerhub.com/rust/how-to-map-values-in-a-rust-hashmap)