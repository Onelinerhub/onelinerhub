# How to merge hashmaps in Rust
// plain

Merging two hashmaps in Rust can be done using the `.extend()` method. This method takes an iterator of key-value pairs and adds them to the hashmap.

## Code example:
```
let mut map1 = hashmap!{
    "a" => 1,
    "b" => 2,
};

let mut map2 = hashmap!{
    "c" => 3,
    "d" => 4,
};

map1.extend(map2);
```

### Output
`map1` will now contain the key-value pairs from both `map1` and `map2`:
`{"a": 1, "b": 2, "c": 3, "d": 4}`

## Explanation:
- `let mut map1 = hashmap!{...}`: creates a mutable hashmap `map1` with the given key-value pairs
- `let mut map2 = hashmap!{...}`: creates a mutable hashmap `map2` with the given key-value pairs
- `map1.extend(map2)`: adds the key-value pairs from `map2` to `map1`

## Helpful links:
- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Documentation - extend()](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.extend)