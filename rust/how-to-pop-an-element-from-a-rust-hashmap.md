# How to pop an element from a Rust HashMap?
// plain

To pop an element from a Rust HashMap, you can use the `remove` method. This method takes a key as an argument and returns the corresponding value if it exists.

## Example code

```rust
let mut map = HashMap::new();
map.insert("key1", "value1");
map.insert("key2", "value2");

let value = map.remove("key1");
```

## Output example

```
Some("value1")
```

## Code explanation

- `let mut map = HashMap::new();`: creates a new empty HashMap
- `map.insert("key1", "value1");`: inserts a key-value pair into the HashMap
- `map.insert("key2", "value2");`: inserts another key-value pair into the HashMap
- `let value = map.remove("key1");`: removes the key-value pair with the key "key1" from the HashMap and stores the value in the variable `value`

## Helpful links
- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to pop an element from a Rust HashMap?](https://onelinerhub.com/rust/how-to-pop-an-element-from-a-rust-hashmap)