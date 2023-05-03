# How to read YAML from string in Rust
// plain

Reading YAML from string in Rust can be done using the [serde_yaml](https://crates.io/crates/serde_yaml) crate.

Example code:
```rust
use serde_yaml;

let yaml_str = "
key1: value1
key2: value2
";

let data: serde_yaml::Value = serde_yaml::from_str(yaml_str).unwrap();

println!("{:#?}", data);
```

## Output example
```
Object({
    key1: String("value1"),
    key2: String("value2"),
})
```

Code parts:
- `use serde_yaml;`: imports the serde_yaml crate
- `let yaml_str = "...";`: creates a string containing YAML data
- `let data: serde_yaml::Value = serde_yaml::from_str(yaml_str).unwrap();`: parses the YAML string into a `serde_yaml::Value`
- `println!("{:#?}", data);`: prints the parsed data in a human-readable format

## Helpful links
- [serde_yaml crate](https://crates.io/crates/serde_yaml)

group: rust-yaml