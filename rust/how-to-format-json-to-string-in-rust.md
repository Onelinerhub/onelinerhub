# How to format json to string in Rust
// plain

The `serde_json` crate provides a `to_string` method to format a json object to a string.

Example code:
```rust
use serde_json::json;

let json_object = json!({
    "name": "John Doe",
    "age": 30
});

let json_string = json_object.to_string();
```

### Output
```
{"name":"John Doe","age":30}
```

Explanation:
- `use serde_json::json;`: imports the `json` macro from the `serde_json` crate
- `let json_object = json!({...});`: creates a json object from the given data
- `let json_string = json_object.to_string();`: formats the json object to a string

## Helpful links:
- [serde_json crate documentation](https://docs.serde.rs/serde_json/)
- [json! macro documentation](https://docs.serde.rs/serde_json/macro.json.html)