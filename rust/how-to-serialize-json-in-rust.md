# How to serialize JSON in Rust?
// plain

Serializing JSON in Rust is done using the `serde` crate. `serde` provides a powerful framework for serializing and deserializing data structures.

## Example code

```rust
extern crate serde;
extern crate serde_json;

use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
}

fn main() {
    let person = Person {
        name: "John".to_string(),
        age: 30,
    };

    let serialized = serde_json::to_string(&person).unwrap();

    println!("serialized = {}", serialized);
}
```

## Output example

```
serialized = {"name":"John","age":30}
```

## Code explanation

- `extern crate serde;` and `extern crate serde_json;`: imports the `serde` and `serde_json` crates.
- `#[derive(Serialize, Deserialize)]`: derives the `Serialize` and `Deserialize` traits for the `Person` struct.
- `serde_json::to_string(&person).unwrap()`: serializes the `person` struct into a JSON string.

## Helpful links
- [serde crate](https://crates.io/crates/serde)
- [serde_json crate](https://crates.io/crates/serde_json)
- [serde documentation](https://docs.serde.rs/)

group: rust-json

onelinerhub: [How to serialize JSON in Rust?](https://onelinerhub.com/rust/how-to-serialize-json-in-rust)