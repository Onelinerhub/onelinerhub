# How to read YAML file in Rust
// plain

Reading YAML files in Rust is easy with the [serde_yaml](https://crates.io/crates/serde_yaml) crate. To read a YAML file, first add the crate to your `Cargo.toml` file:

```
[dependencies]
serde_yaml = "1.0"
```

Then, use the `from_reader` method to read the YAML file into a Rust data structure:

```rust
use std::fs::File;
use serde_yaml;

let file = File::open("example.yaml")?;
let data: serde_yaml::Value = serde_yaml::from_reader(file)?;
```

The `serde_yaml::Value` type is a generic type that can represent any valid YAML data structure. You can then use the `as_*` methods to convert the `Value` into the desired Rust type.

- `serde_yaml::from_reader`: Reads a YAML file into a `serde_yaml::Value`
- `Value::as_*`: Converts a `Value` into a Rust type

## Helpful links
- [serde_yaml crate](https://crates.io/crates/serde_yaml)
- [serde_yaml documentation](https://docs.rs/serde_yaml/1.0.0/serde_yaml/)

group: rust-yaml