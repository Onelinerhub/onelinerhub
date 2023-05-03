# Rust YAML parser example
// plain

[serde_yaml](https://crates.io/crates/serde_yaml) is a Rust library for parsing and serializing YAML. Here is an example of how to parse a YAML string:

```rust
use serde_yaml;

let yaml_str = "
name: John
age: 30
";

let data: serde_yaml::Value = serde_yaml::from_str(yaml_str).unwrap();

println!("Name: {}", data["name"].as_str().unwrap());
println!("Age: {}", data["age"].as_i64().unwrap());
```

This code will ## Output example
```
Name: John
Age: 30
```

The code consists of the following parts:

1. `use serde_yaml`: This imports the serde_yaml library.
2. `let yaml_str = ...`: This creates a string containing the YAML data.
3. `let data: serde_yaml::Value = serde_yaml::from_str(yaml_str).unwrap()`: This parses the YAML string and stores the result in a `serde_yaml::Value` object.
4. `println!("Name: {}", data["name"].as_str().unwrap())`: This prints the value of the `name` key as a string.
5. `println!("Age: {}", data["age"].as_i64().unwrap())`: This prints the value of the `age` key as an integer.

## Helpful links

- [serde_yaml](https://crates.io/crates/serde_yaml)
- [YAML Syntax](https://yaml.org/spec/1.2/spec.html)

group: rust-yaml