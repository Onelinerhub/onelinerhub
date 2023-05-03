# How to convert YAML to struct in Rust
// plain

YAML (YAML Ain't Markup Language) is a human-readable data serialization language that can be used to convert data into a variety of data structures. In Rust, the `serde_yaml` crate can be used to convert YAML into a Rust struct.

Example code:
```rust
use serde::{Deserialize, Serialize};
use serde_yaml;

#[derive(Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
}

fn main() {
    let yaml = r#"
        name: John
        age: 30
    "#;

    let person: Person = serde_yaml::from_str(yaml).unwrap();
    println!("{:?}", person);
}
```

## Output example
```
Person { name: "John", age: 30 }
```

Code parts with detailed ## Explanation


1. `use serde::{Deserialize, Serialize};`: This imports the `Deserialize` and `Serialize` traits from the `serde` crate, which are needed to convert YAML into a Rust struct.

2. `#[derive(Serialize, Deserialize)]`: This is a Rust attribute macro that automatically implements the `Serialize` and `Deserialize` traits for the `Person` struct.

3. `let yaml = r#" ... "#;`: This creates a string literal containing the YAML data.

4. `let person: Person = serde_yaml::from_str(yaml).unwrap();`: This uses the `from_str` method from the `serde_yaml` crate to convert the YAML string into a `Person` struct.

5. `println!("{:?}", person);`: This prints the `Person` struct to the console.

## Helpful links

- [serde_yaml crate](https://crates.io/crates/serde_yaml)
- [serde crate](https://crates.io/crates/serde)

group: rust-yaml