# How to convert a Rust HashMap to JSON?
// plain

Converting a Rust HashMap to JSON can be done using the `serde` crate. `serde` provides a `Serialize` trait which can be used to serialize a Rust data structure into a JSON string.

## Example code

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
}

fn main() {
    let mut map = std::collections::HashMap::new();
    map.insert("John", Person {
        name: "John".to_string(),
        age: 30,
    });
    map.insert("Alice", Person {
        name: "Alice".to_string(),
        age: 25,
    });

    let json = serde_json::to_string(&map).unwrap();
    println!("{}", json);
}
```

## Output example

```json
{"John":{"name":"John","age":30},"Alice":{"name":"Alice","age":25}}
```

## Code explanation


1. `use serde::{Serialize, Deserialize};`: This imports the `Serialize` and `Deserialize` traits from the `serde` crate.

2. `#[derive(Serialize, Deserialize)]`: This derives the `Serialize` and `Deserialize` traits for the `Person` struct.

3. `let json = serde_json::to_string(&map).unwrap();`: This uses the `serde_json` crate to serialize the `map` into a JSON string.

4. `println!("{}", json);`: This prints the JSON string to the console.

## Helpful links

- [serde](https://serde.rs/)
- [serde_json](https://docs.serde.rs/serde_json/)

group: rust-hashmap

onelinerhub: [How to convert a Rust HashMap to JSON?](https://onelinerhub.com/rust/how-to-convert-a-rust-hashmap-to-json)