# How to borrow hashmap in Rust
// plain

HashMap is a data structure in Rust that allows you to store key-value pairs. To borrow a HashMap, you can use the `borrow()` method. This will return a `Ref<HashMap>` which is a reference to the HashMap.

Example:
```rust
let mut map = HashMap::new();
map.insert("key", "value");

let borrowed_map = map.borrow();
```

The `borrow()` method returns a `Ref<HashMap>` which is a reference to the HashMap. This reference can be used to access the data stored in the HashMap.

## Code explanation

- `let mut map = HashMap::new();`: creates a new HashMap
- `map.insert("key", "value");`: inserts a key-value pair into the HashMap
- `let borrowed_map = map.borrow();`: borrows the HashMap and stores it in the `borrowed_map` variable

## Helpful links
- [Rust HashMap Documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)

group: rust-borrow