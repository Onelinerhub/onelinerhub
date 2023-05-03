# How to write YAML to file in Rust
// plain

Writing YAML to file in Rust is easy with the [serde_yaml](https://docs.rs/serde_yaml/0.8.13/serde_yaml/) crate.

Example code:
```rust
use serde_yaml;

let data = vec![1, 2, 3];

let serialized = serde_yaml::to_string(&data).unwrap();

std::fs::write("data.yaml", serialized).unwrap();
```

## Output example
```
[1, 2, 3]
```

Code parts:

1. `use serde_yaml;` - imports the serde_yaml crate.
2. `let data = vec![1, 2, 3];` - creates a vector of data to be serialized.
3. `let serialized = serde_yaml::to_string(&data).unwrap();` - serializes the data into a YAML string.
4. `std::fs::write("data.yaml", serialized).unwrap();` - writes the serialized data to a file named `data.yaml`.

## Helpful links

- [serde_yaml](https://docs.rs/serde_yaml/0.8.13/serde_yaml/) - crate documentation.
- [std::fs::write](https://doc.rust-lang.org/std/fs/fn.write.html) - documentation for the `write` function.

group: rust-yaml