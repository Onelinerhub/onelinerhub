# How to create a Rust HashMap from a vec?
// plain

Creating a Rust HashMap from a vec is a simple process. The following example code creates a HashMap from a vec of tuples:

```rust
let mut map = HashMap::new();
let vec = vec![("key1", "value1"), ("key2", "value2")];

for (key, value) in vec {
    map.insert(key, value);
}
```

The output of the example code is a HashMap with two entries:

```
{"key1": "value1", "key2": "value2"}
```

## Code explanation


1. `let mut map = HashMap::new();` - creates a new, empty HashMap.
2. `let vec = vec![("key1", "value1"), ("key2", "value2")];` - creates a vec of tuples.
3. `for (key, value) in vec {` - iterates over the vec of tuples.
4. `map.insert(key, value);` - inserts each tuple into the HashMap.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Vec Documentation](https://doc.rust-lang.org/std/vec/struct.Vec.html)

group: rust-hashmap

onelinerhub: [How to create a Rust HashMap from a vec?](https://onelinerhub.com/rust/how-to-create-a-rust-hashmap-from-a-vec)