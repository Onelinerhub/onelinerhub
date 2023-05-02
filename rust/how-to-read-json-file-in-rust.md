# How to read JSON file in Rust
// plain

Reading a JSON file in Rust is relatively straightforward. First, you need to use the `serde_json` crate to parse the JSON file. Then, you can use the `serde::Deserialize` trait to deserialize the JSON data into a Rust struct. Finally, you can use the `serde::Serialize` trait to serialize the data back into a JSON string. The following ## Code example shows how to read a JSON file and deserialize it into a Rust struct:

```rust
use serde::{Deserialize, Serialize};
use serde_json::Result;

#[derive(Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
    phones: Vec<String>,
}

fn main() -> Result<()> {
    // Open the file in read-only mode with buffer.
    let file = std::fs::File::open("person.json")?;
    let reader = std::io::BufReader::new(file);

    // Read the JSON contents of the file as an instance of `Person`.
    let p: Person = serde_json::from_reader(reader)?;

    println!("{} is {} years old", p.name, p.age);

    // Convert `Person` back to a JSON string.
    let j = serde_json::to_string(&p)?;

    println!("{}", j);
    Ok(())
}
```

The output of the above ## Code example would be:

```
John is 30 years old
{"name":"John","age":30,"phones":["555-1234","555-2345"]}
```

The `serde_json` crate provides the `serde::Deserialize` and `serde::Serialize` traits which allow you to easily deserialize and serialize JSON data into Rust structs. The `serde_json::from_reader` function is used to read the JSON file and deserialize it into a Rust struct. The `serde_json::to_string` function is used to serialize the data back into a JSON string.

## Helpful links
- [serde_json crate](https://docs.rs/serde_json/1.0.50/serde_json/)
- [serde::Deserialize trait](https://docs.rs/serde/1.0.104/serde/trait.Deserialize.html)
- [serde::Serialize trait](https://docs.rs/serde/1.0.104/serde/trait.Serialize.html)

group: rust-files