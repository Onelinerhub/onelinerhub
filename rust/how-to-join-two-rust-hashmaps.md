# How to join two Rust HashMaps?
// plain

Joining two Rust HashMaps can be done using the `extend()` method. This method takes ownership of the parameter and appends its key-value pairs to the original HashMap.

```rust
let mut map1 = HashMap::new();
map1.insert("a", 1);
map1.insert("b", 2);

let mut map2 = HashMap::new();
map2.insert("c", 3);
map2.insert("d", 4);

map1.extend(map2);

println!("{:?}", map1);
```

## Output example

```
{"a": 1, "b": 2, "c": 3, "d": 4}
```

## Code explanation


1. `let mut map1 = HashMap::new();` - creates a new empty HashMap called `map1`
2. `map1.insert("a", 1);` - inserts a key-value pair into `map1`
3. `map1.extend(map2);` - takes ownership of `map2` and appends its key-value pairs to `map1`
4. `println!("{:?}", map1);` - prints the contents of `map1`

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to join two Rust HashMaps?](https://onelinerhub.com/rust/how-to-join-two-rust-hashmaps)