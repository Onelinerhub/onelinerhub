# How to drain a Rust HashMap?
// plain

A Rust HashMap can be drained using the `drain` method. This method returns an iterator over the key-value pairs in the map, which can then be used to remove the elements from the map.

## Example code

```rust
let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);

for (key, value) in map.drain() {
    println!("key: {} value: {}", key, value);
}
```

## Output example

```
key: a value: 1
key: b value: 2
```

## Code explanation


1. `let mut map = HashMap::new();` - This line creates a new empty HashMap.
2. `map.insert("a", 1);` - This line inserts a key-value pair into the HashMap.
3. `for (key, value) in map.drain() {` - This line creates an iterator over the key-value pairs in the map.
4. `println!("key: {} value: {}", key, value);` - This line prints out the key-value pairs.
5. `}` - This line ends the loop.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to drain a Rust HashMap?](https://onelinerhub.com/rust/how-to-drain-a-rust-hashmap)