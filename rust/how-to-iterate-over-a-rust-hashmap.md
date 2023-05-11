# How to iterate over a Rust HashMap?
// plain

Iterating over a Rust HashMap can be done using the `iter()` method. This method returns an iterator over the key-value pairs of the map.

## Example code

```
let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);

for (key, value) in map.iter() {
    println!("key: {} value: {}", key, value);
}
```

## Output example

```
key: a value: 1
key: b value: 2
```

## Code explanation

- `let mut map = HashMap::new();`: creates a new empty HashMap
- `map.insert("a", 1);`: inserts a key-value pair into the HashMap
- `map.iter()`: returns an iterator over the key-value pairs of the map
- `for (key, value) in map.iter()`: iterates over the key-value pairs of the map
- `println!("key: {} value: {}", key, value);`: prints the key and value of the current iteration

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to iterate over a Rust HashMap?](https://onelinerhub.com/rust/how-to-iterate-over-a-rust-hashmap)