# How to use a tuple as a key in a Rust HashMap?
// plain

Tuples can be used as keys in a Rust HashMap by implementing the `Hash` and `Eq` traits. This can be done by using the `#[derive(Hash, Eq)]` annotation on the tuple struct.

```rust
#[derive(Hash, Eq)]
struct TupleStruct(i32, i32);

use std::collections::HashMap;

let mut map = HashMap::new();

let key = TupleStruct(1, 2);

map.insert(key, "value");
```

The example code above creates a tuple struct `TupleStruct` with two `i32` fields, and implements the `Hash` and `Eq` traits on it. Then, a `HashMap` is created and a key is created from the `TupleStruct`. Finally, the key is used to insert a value into the `HashMap`.

- `#[derive(Hash, Eq)]`: Annotation to implement the `Hash` and `Eq` traits on a tuple struct.
- `TupleStruct(i32, i32)`: Tuple struct with two `i32` fields.
- `HashMap::new()`: Creates a new `HashMap`.
- `let key = TupleStruct(1, 2)`: Creates a key from the `TupleStruct`.
- `map.insert(key, "value")`: Inserts a value into the `HashMap` using the key.

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Derive Documentation](https://doc.rust-lang.org/reference/attributes/derive.html)

group: rust-hashmap

onelinerhub: [How to use a tuple as a key in a Rust HashMap?](https://onelinerhub.com/rust/how-to-use-a-tuple-as-a-key-in-a-rust-hashmap)