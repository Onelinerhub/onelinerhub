# How to convert a Rust HashMap to a JSON string?
// plain

To convert a Rust HashMap to a JSON string, you can use the `serde_json` crate.

## Example code

```rust
use serde_json::json;

let mut map = HashMap::new();
map.insert("key1", "value1");
map.insert("key2", "value2");

let json_string = json!(map).to_string();
```

## Output example

```
"{"key1":"value1","key2":"value2"}"
```

## Code explanation

- `use serde_json::json;`: imports the `json` function from the `serde_json` crate.
- `let mut map = HashMap::new();`: creates a new empty `HashMap`.
- `map.insert("key1", "value1");`: inserts a key-value pair into the `HashMap`.
- `let json_string = json!(map).to_string();`: converts the `HashMap` to a JSON string.

## Helpful links
- [serde_json crate](https://crates.io/crates/serde_json)
- [serde_json documentation](https://docs.serde.rs/serde_json/)

group: rust-hashmap

onelinerhub: [How to convert a Rust HashMap to a JSON string?](https://onelinerhub.com/rust/how-to-convert-a-rust-hashmap-to-a-json-string)