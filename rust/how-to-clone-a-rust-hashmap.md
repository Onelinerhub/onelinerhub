# How to clone a Rust HashMap?
// plain

Cloning a Rust HashMap is a simple process. It can be done using the `clone()` method.

```rust
let mut map1 = HashMap::new();
map1.insert("a", 1);
map1.insert("b", 2);

let map2 = map1.clone();
```

This will create a new `HashMap` called `map2` which is a clone of `map1`.

## Code explanation


1. `let mut map1 = HashMap::new();` - creates a new `HashMap` called `map1`
2. `map1.insert("a", 1);` - inserts a key-value pair into `map1`
3. `map1.insert("b", 2);` - inserts another key-value pair into `map1`
4. `let map2 = map1.clone();` - creates a clone of `map1` called `map2`

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to clone a Rust HashMap?](https://onelinerhub.com/rust/how-to-clone-a-rust-hashmap)