# How to join hashmaps in Rust
// plain

Joining two hashmaps in Rust can be done using the `extend` method. This method takes an iterator of key-value pairs and adds them to the existing hashmap.

## Code example:
```
let mut map1 = hashmap!{
    "a" => 1,
    "b" => 2,
};

let map2 = hashmap!{
    "c" => 3,
    "d" => 4,
};

map1.extend(map2);
```

### Output
`map1` now contains the key-value pairs `{"a": 1, "b": 2, "c": 3, "d": 4}`

Explanation:
- `let mut map1 = hashmap!{...}`: creates a mutable hashmap `map1` with the given key-value pairs
- `let map2 = hashmap!{...}`: creates a hashmap `map2` with the given key-value pairs
- `map1.extend(map2)`: adds the key-value pairs from `map2` to `map1`

## Helpful links:
- [HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Extend Method Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.extend)