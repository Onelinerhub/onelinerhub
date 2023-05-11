# How to convert JSON to a struct in Rust?
// plain

JSON can be converted to a struct in Rust using the `serde` crate. The `serde` crate provides a `Deserialize` trait which can be used to convert JSON data into a Rust struct.

## Example code

```rust
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
    phones: Vec<String>,
}

fn main() {
    // Some JSON input data as a &str. Maybe this comes from the user.
    let data = r#"
        {
            "name": "John Doe",
            "age": 43,
            "phones": [
                "+44 1234567",
                "+44 2345678"
            ]
        }"#;

    // Parse the string of data into a Person object. This is exactly the
    // same function as the one that produced serde_json::Value above, but
    // now we are asking it for a Person as output.
    let p: Person = serde_json::from_str(data).unwrap();

    // Do things just like with any other Rust data structure.
    println!("Please call {} at the number {}", p.name, p.phones[0]);
}
```

## Output example

```
Please call John Doe at the number +44 1234567
```

## Code explanation


1. `use serde::{Deserialize, Serialize};`: This imports the `Deserialize` and `Serialize` traits from the `serde` crate.

2. `#[derive(Serialize, Deserialize)]`: This is a Rust attribute which tells the compiler to generate code for the `Serialize` and `Deserialize` traits for the `Person` struct.

3. `let p: Person = serde_json::from_str(data).unwrap();`: This line uses the `serde_json::from_str` function to parse the JSON data into a `Person` struct.

## Helpful links

- [serde crate](https://crates.io/crates/serde)
- [serde_json crate](https://crates.io/crates/serde_json)
- [serde documentation](https://serde.rs/)

group: rust-json

onelinerhub: [How to convert JSON to a struct in Rust?](https://onelinerhub.com/rust/how-to-convert-json-to-a-struct-in-rust)