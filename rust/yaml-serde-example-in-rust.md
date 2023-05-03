# YAML serde example in Rust
// plain

YAML is a popular data serialization format that is used to store data in a human-readable format. Rust provides a library called `serde_yaml` which can be used to serialize and deserialize YAML data.

Example code:
```rust
use serde::{Deserialize, Serialize};
use serde_yaml;

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

    let serialized = serde_yaml::to_string(&person).unwrap();
    println!("Serialized: {}", serialized);

    let deserialized: Person = serde_yaml::from_str(&serialized).unwrap();
    println!("Deserialized: {:?}", deserialized);
}
```

## Output example
```
Serialized: age: 30
name: John

Deserialized: Person { name: "John", age: 30 }
```

Code parts with detailed ## Explanation

- `use serde::{Deserialize, Serialize};`: This imports the `Serialize` and `Deserialize` traits from the `serde` crate. These traits are used to define the data structure that will be serialized and deserialized.
- `#[derive(Serialize, Deserialize)]`: This is a Rust macro that automatically implements the `Serialize` and `Deserialize` traits for the `Person` struct.
- `serde_yaml::to_string(&person).unwrap()`: This uses the `serde_yaml` crate to serialize the `person` struct into a YAML string.
- `serde_yaml::from_str(&serialized).unwrap()`: This uses the `serde_yaml` crate to deserialize the YAML string into a `Person` struct.

## Helpful links
- [serde_yaml crate](https://crates.io/crates/serde_yaml)
- [serde crate](https://crates.io/crates/serde)

group: rust-yaml