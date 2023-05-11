# How to get a value by key from JSON in Rust?
// plain

Getting a value by key from JSON in Rust is easy with the `serde_json` crate.

## Example code

```rust
extern crate serde_json;

fn main() {
    let data = r#"
        {
            "name": "John Doe",
            "age": 43
        }
    "#;

    let v: serde_json::Value = serde_json::from_str(data).unwrap();
    let name = v["name"].as_str().unwrap();

    println!("Name: {}", name);
}
```

## Output example

```
Name: John Doe
```

The code above:
- imports the `serde_json` crate (`extern crate serde_json;`)
- creates a JSON string (`let data = r#"{...}"#;`)
- parses the JSON string into a `serde_json::Value` (`let v: serde_json::Value = serde_json::from_str(data).unwrap();`)
- gets the value of the `name` key (`let name = v["name"].as_str().unwrap();`)
- prints the value of the `name` key (`println!("Name: {}", name);`)

## Helpful links
- [serde_json crate](https://crates.io/crates/serde_json)
- [serde_json documentation](https://docs.serde.rs/serde_json/)

group: rust-json

onelinerhub: [How to get a value by key from JSON in Rust?](https://onelinerhub.com/rust/how-to-get-a-value-by-key-from-json-in-rust)