# How to create a HashMap of pointers in Rust?
// plain

A HashMap of pointers in Rust can be created using the `HashMap` type from the `std::collections` module.

```rust
use std::collections::HashMap;

let mut map: HashMap<&str, *const i32> = HashMap::new();

let a = 10;
let b = 20;

map.insert("a", &a);
map.insert("b", &b);
```

The code above creates a `HashMap` with `&str` keys and `*const i32` values. The `&a` and `&b` are references to the `i32` variables `a` and `b`.

- `use std::collections::HashMap`: imports the `HashMap` type from the `std::collections` module.
- `let mut map: HashMap<&str, *const i32> = HashMap::new();`: creates a `HashMap` with `&str` keys and `*const i32` values.
- `map.insert("a", &a);`: inserts a key-value pair into the `HashMap`, with the key being `"a"` and the value being a pointer to the `i32` variable `a`.
- `map.insert("b", &b);`: inserts a key-value pair into the `HashMap`, with the key being `"b"` and the value being a pointer to the `i32` variable `b`.

## Helpful links
- [HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-hashmap

onelinerhub: [How to create a HashMap of pointers in Rust?](https://onelinerhub.com/rust/how-to-create-a-hashmap-of-pointers-in-rust)