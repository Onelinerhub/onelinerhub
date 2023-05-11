# How to create a HashMap of HashMaps in Rust?
// plain

A HashMap of HashMaps can be created in Rust using the `HashMap::new()` method. The following example code creates a HashMap of HashMaps with `String` keys and `i32` values:

```rust
use std::collections::HashMap;

let mut map_of_maps: HashMap<String, HashMap<String, i32>> = HashMap::new();

let mut inner_map1: HashMap<String, i32> = HashMap::new();
inner_map1.insert(String::from("key1"), 1);
inner_map1.insert(String::from("key2"), 2);

let mut inner_map2: HashMap<String, i32> = HashMap::new();
inner_map2.insert(String::from("key3"), 3);
inner_map2.insert(String::from("key4"), 4);

map_of_maps.insert(String::from("map1"), inner_map1);
map_of_maps.insert(String::from("map2"), inner_map2);

println!("{:?}", map_of_maps);
```

## Output example

```
{"map1": {"key1": 1, "key2": 2}, "map2": {"key3": 3, "key4": 4}}
```

## Code explanation


1. `use std::collections::HashMap;` - imports the `HashMap` type from the `std::collections` module.

2. `let mut map_of_maps: HashMap<String, HashMap<String, i32>> = HashMap::new();` - creates a `HashMap` with `String` keys and `HashMap` values, where the `HashMap` values have `String` keys and `i32` values.

3. `let mut inner_map1: HashMap<String, i32> = HashMap::new();` - creates a `HashMap` with `String` keys and `i32` values.

4. `inner_map1.insert(String::from("key1"), 1);` - inserts a key-value pair into the `inner_map1` `HashMap`.

5. `map_of_maps.insert(String::from("map1"), inner_map1);` - inserts a key-value pair into the `map_of_maps` `HashMap`, where the value is the `inner_map1` `HashMap`.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to create a HashMap of HashMaps in Rust?](https://onelinerhub.com/rust/how-to-create-a-hashmap-of-hashmaps-in-rust)