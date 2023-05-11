# How to implement PartialEq for a Rust HashMap?
// plain

To implement `PartialEq` for a Rust `HashMap`, you can use the `eq` method provided by the `HashMap` type. This method takes two `HashMap`s as arguments and returns `true` if they contain the same key-value pairs.

## Example code

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


1. `use std::collections::HashMap;`: imports the `HashMap` type from the `std::collections` module.

2. `let mut map1 = HashMap::new();`: creates a new `HashMap` called `map1`.

3. `map1.insert("a", 1);`: inserts a key-value pair into `map1`, with the key being `"a"` and the value being `1`.

4. `let mut map2 = HashMap::new();`: creates a new `HashMap` called `map2`.

5. `map2.insert("a", 1);`: inserts a key-value pair into `map2`, with the key being `"a"` and the value being `1`.

6. `assert!(map1.eq(&map2));`: uses the `eq` method to compare `map1` and `map2` and returns `true` if they contain the same key-value pairs.

## Helpful links

- [Rust Documentation - HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to implement PartialEq for a Rust HashMap?](https://onelinerhub.com/rust/how-to-implement-partialeq-for-a-rust-hashmap)