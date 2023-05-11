# How to convert struct to JSON string in Rust?
// plain

Converting a struct to a JSON string in Rust can be done using the `serde` crate. `serde` provides a set of macros to serialize and deserialize data structures to and from JSON.

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

    let json_string = serde_json::to_string(&person).unwrap();
    println!("{}", json_string);
}
```

## Output example

```
{"name":"John","age":30}
```

## Code explanation

- `use serde::{Serialize, Deserialize};`: imports the `Serialize` and `Deserialize` traits from the `serde` crate.
- `#[derive(Serialize, Deserialize)]`: derives the `Serialize` and `Deserialize` traits for the `Person` struct.
- `serde_json::to_string(&person).unwrap()`: serializes the `person` struct to a JSON string.

## Helpful links
- [serde crate](https://crates.io/crates/serde)
- [serde_json crate](https://crates.io/crates/serde_json)

group: rust-json

onelinerhub: [How to convert struct to JSON string in Rust?](https://onelinerhub.com/rust/how-to-convert-struct-to-json-string-in-rust)