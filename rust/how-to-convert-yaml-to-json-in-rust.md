# How to convert YAML to JSON in Rust
// plain

YAML to JSON conversion in Rust can be done using the [serde_yaml](https://crates.io/crates/serde_yaml) crate. This crate provides a `from_str` function which can be used to convert a YAML string to a JSON string.

Example code:
```rust
use serde_yaml;

let yaml_string = "
name: John
age: 30
";

let json_string = serde_yaml::from_str(yaml_string).unwrap();

println!("{}", json_string);
```

## Output example
```json
{"name":"John","age":30}
```

Code parts with detailed ## Explanation


1. `use serde_yaml;`: This imports the `serde_yaml` crate.

2. `let yaml_string = "name: John\nage: 30\n";`: This creates a YAML string with two fields, `name` and `age`.

3. `let json_string = serde_yaml::from_str(yaml_string).unwrap();`: This uses the `from_str` function from the `serde_yaml` crate to convert the YAML string to a JSON string.

4. `println!("{}", json_string);`: This prints the JSON string to the console.

## Helpful links

- [serde_yaml](https://crates.io/crates/serde_yaml)

group: rust-yaml