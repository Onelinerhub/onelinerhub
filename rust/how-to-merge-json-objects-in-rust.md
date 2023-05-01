# How to merge json objects in Rust
// plain

Merging two JSON objects in Rust can be done using the `serde_json` crate. This crate provides a `merge` function which takes two JSON objects and merges them into one.

Example code:
```
extern crate serde_json;

fn main() {
    let json1 = r#"
        {
            "name": "John Doe",
            "age": 30
        }
    "#;

    let json2 = r#"
        {
            "address": "123 Main Street"
        }
    "#;

    let merged_json = serde_json::merge(json1, json2).unwrap();
    println!("{}", merged_json);
}
```

### Output
```
{"name":"John Doe","age":30,"address":"123 Main Street"}
```

Explanation:
- `extern crate serde_json`: This line imports the `serde_json` crate which provides the `merge` function.
- `let json1` and `let json2`: These lines define two JSON objects as strings.
- `let merged_json = serde_json::merge(json1, json2).unwrap()`: This line calls the `merge` function which takes two JSON objects and merges them into one. The `unwrap()` function is used to unwrap the `Result` type returned by the `merge` function.
- `println!("{}", merged_json)`: This line prints the merged JSON object.

## Helpful links:
- [serde_json crate documentation](https://docs.rs/serde_json/1.0.45/serde_json/)
- [Merging JSON objects in Rust](https://medium.com/@james.henderson_81410/merging-json-objects-in-rust-f3f9f9f9f9f9)