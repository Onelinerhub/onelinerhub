# How to serialize struct to json in Rust
// plain

Serializing a struct to JSON in Rust can be done using the `serde` crate. This crate provides a `Serialize` trait that can be implemented for a struct to enable serialization.

## Example code

```rust
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


1. `use serde::{Serialize, Deserialize};` - This imports the `Serialize` and `Deserialize` traits from the `serde` crate.

2. `#[derive(Serialize, Deserialize)]` - This macro derives the `Serialize` and `Deserialize` traits for the `Person` struct.

3. `let serialized = serde_json::to_string(&person).unwrap();` - This line serializes the `person` struct to a JSON string using the `serde_json` crate.

4. `println!("serialized = {}", serialized);` - This line prints the serialized JSON string to the console.

## Helpful links

- [serde crate](https://crates.io/crates/serde)
- [serde_json crate](https://crates.io/crates/serde_json)

group: rust-struct