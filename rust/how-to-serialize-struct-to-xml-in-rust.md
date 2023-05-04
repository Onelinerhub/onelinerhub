# How to serialize struct to xml in Rust
// plain

Serializing a struct to XML in Rust can be done using the [serde](https://serde.rs/) crate.

## Example code

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
}

fn main() {
    let person = Person {
        name: "John".to_string(),
        age: 30,
    };

    let xml = serde_xml_rs::to_string(&person).unwrap();
    println!("{}", xml);
}
```

## Output example

```xml
<Person><name>John</name><age>30</age></Person>
```

The code above uses the `serde` crate to serialize a struct to XML. The `#[derive(Serialize, Deserialize)]` attribute is used to enable serialization and deserialization of the struct. The `serde_xml_rs::to_string` function is then used to serialize the struct to XML.

## Helpful links

- [serde](https://serde.rs/)
- [serde_xml_rs](https://docs.rs/serde_xml_rs/0.9.0/serde_xml_rs/)

group: rust-struct