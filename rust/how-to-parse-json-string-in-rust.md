# How to parse JSON string in Rust?
// plain

Parsing JSON string in Rust can be done using the `serde` crate. `serde` is a powerful library for serializing and deserializing data structures.

## Example code

```rust
extern crate serde;
extern crate serde_json;

use serde_json::{Result, Value};

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

    // Parse the string of data into serde_json::Value.
    let v: Value = serde_json::from_str(data)?;

    // Access parts of the data by indexing with square brackets.
    println!("Please call {} at the number {}", v["name"], v["phones"][0]);
}
```

## Output example

```
Please call John Doe at the number +44 1234567
```

## Code explanation


1. `extern crate serde;` and `extern crate serde_json;`: These two lines are used to import the `serde` and `serde_json` crates.

2. `use serde_json::{Result, Value};`: This line imports the `Result` and `Value` types from the `serde_json` crate.

3. `let data = r#" ... "#;`: This line creates a string literal containing the JSON data.

4. `let v: Value = serde_json::from_str(data)?;`: This line parses the JSON data into a `Value` type.

5. `println!("Please call {} at the number {}", v["name"], v["phones"][0]);`: This line prints out the parsed data.

## Helpful links

- [serde](https://crates.io/crates/serde)
- [serde_json](https://crates.io/crates/serde_json)

group: rust-json

onelinerhub: [How to parse JSON string in Rust?](https://onelinerhub.com/rust/how-to-parse-json-string-in-rust)