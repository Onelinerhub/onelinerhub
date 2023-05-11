# How to compare two Rust HashMaps?
// plain

Comparing two Rust HashMaps can be done using the `eq` method. This method takes two `HashMap`s as arguments and returns `true` if they contain the same key-value pairs.

```rust
use std::collections::HashMap;

let mut map1 = HashMap::new();
map1.insert("a", 1);
map1.insert("b", 2);

let mut map2 = HashMap::new();
map2.insert("a", 1);
map2.insert("b", 2);

assert!(map1.eq(&map2));
```

## Output example

```
assertion successful
```

## Code explanation


1. `use std::collections::HashMap`: This imports the `HashMap` type from the `std::collections` module.

2. `let mut map1 = HashMap::new()`: This creates a new empty `HashMap` called `map1`.

3. `map1.insert("a", 1)`: This inserts a key-value pair into `map1`, with the key being `"a"` and the value being `1`.

4. `map2.insert("a", 1)`: This inserts a key-value pair into `map2`, with the key being `"a"` and the value being `1`.

5. `assert!(map1.eq(&map2))`: This uses the `eq` method to compare `map1` and `map2`. If they contain the same key-value pairs, it will return `true`.

## Helpful links

- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to compare two Rust HashMaps?](https://onelinerhub.com/rust/how-to-compare-two-rust-hashmaps)