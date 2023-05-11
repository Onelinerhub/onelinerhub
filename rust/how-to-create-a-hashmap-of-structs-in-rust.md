# How to create a HashMap of structs in Rust?
// plain

A HashMap of structs in Rust can be created using the `HashMap` type from the `std::collections` module. The `HashMap` type requires a `key` and a `value` type to be specified. The `key` type must implement the `Eq` and `Hash` traits, while the `value` type can be any type.

## Example code

```rust
use std::collections::HashMap;

#[derive(Debug)]
struct Person {
    name: String,
    age: u32,
}

fn main() {
    let mut map = HashMap::new();
    map.insert("John", Person {
        name: "John".to_string(),
        age: 30,
    });
    map.insert("Alice", Person {
        name: "Alice".to_string(),
        age: 25,
    });
    println!("{:?}", map);
}
```

## Output example

```
{"John": Person { name: "John", age: 30 }, "Alice": Person { name: "Alice", age: 25 }}
```

## Code explanation


1. `use std::collections::HashMap;`: This imports the `HashMap` type from the `std::collections` module.
2. `#[derive(Debug)]`: This is a Rust attribute that allows the `Person` struct to be printed to the console.
3. `let mut map = HashMap::new();`: This creates a new `HashMap` with no entries.
4. `map.insert("John", Person { ... });`: This inserts a new entry into the `HashMap` with a `key` of type `&str` and a `value` of type `Person`.
5. `println!("{:?}", map);`: This prints the contents of the `HashMap` to the console.

## Helpful links

- [HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Derive attribute documentation](https://doc.rust-lang.org/reference/attributes/derive.html)

group: rust-hashmap

onelinerhub: [How to create a HashMap of structs in Rust?](https://onelinerhub.com/rust/how-to-create-a-hashmap-of-structs-in-rust)