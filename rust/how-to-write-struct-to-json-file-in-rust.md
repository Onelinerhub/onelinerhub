# How to write struct to json file in Rust
// plain

Writing a struct to a JSON file in Rust is a simple process. The following example code block shows how to do this:

```
use serde::{Serialize, Deserialize};
use serde_json::{Result, Value};

#[derive(Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
    phones: Vec<String>,
}

fn main() -> Result<()> {
    let p = Person {
        name: String::from("John"),
        age: 30,
        phones: vec![String::from("+44 1234567"), String::from("+44 2345678")],
    };

    let j = serde_json::to_string(&p)?;

    println!("{}", j);

    let mut file = std::fs::File::create("person.json")?;
    serde_json::to_writer_pretty(&mut file, &p)?;

    Ok(())
}
```

The output of the example code is:

```
{
  "name": "John",
  "age": 30,
  "phones": [
    "+44 1234567",
    "+44 2345678"
  ]
}
```

The code consists of the following parts:

1. `use serde::{Serialize, Deserialize};` - imports the `Serialize` and `Deserialize` traits from the `serde` crate.
2. `#[derive(Serialize, Deserialize)]` - derives the `Serialize` and `Deserialize` traits for the `Person` struct.
3. `let p = Person { ... }` - creates an instance of the `Person` struct.
4. `let j = serde_json::to_string(&p)?;` - serializes the `Person` struct to a JSON string.
5. `let mut file = std::fs::File::create("person.json")?;` - creates a file called `person.json`.
6. `serde_json::to_writer_pretty(&mut file, &p)?;` - serializes the `Person` struct to the `person.json` file.

## Helpful links

- [serde](https://serde.rs/)
- [serde_json](https://docs.serde.rs/serde_json/)

group: rust-struct