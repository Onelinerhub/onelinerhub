# How to iterate throught JSON in Rust
// plain

Iterating through JSON in Rust can be done using the `serde_json` crate. This crate provides a `Value` type which can be used to represent any valid JSON value. To iterate through a JSON object, you can use the `for` loop and the `as_object` method to access the underlying `HashMap` of the JSON object.

## Example code

```rust
use serde_json::Value;

let json_str = r#"
    {
        "name": "John Doe",
        "age": 43,
        "phones": [
            "+44 1234567",
            "+44 2345678"
        ]
    }
"#;

let json_value: Value = serde_json::from_str(json_str).unwrap();

for (key, value) in json_value.as_object().unwrap() {
    println!("key: {} value: {}", key, value);
}
```

## Output example

```
key: name value: "John Doe"
key: age value: 43
key: phones value: [
    "+44 1234567",
    "+44 2345678"
]
```

## Code explanation

- `serde_json` crate: provides a `Value` type which can be used to represent any valid JSON value
- `for` loop: used to iterate through the JSON object
- `as_object` method: used to access the underlying `HashMap` of the JSON object
- `unwrap` method: used to convert the `Value` type to a `HashMap`

## Helpful links
- [serde_json crate](https://docs.rs/serde_json/1.0.50/serde_json/)
- [JSON and Serde in Rust](https://medium.com/@trevor.e.carroll/json-and-serde-in-rust-part-1-d1f3e2f3b1b2)

group: rust-loops