# How to convert struct to bytes in Rust
// plain

Structs in Rust can be converted to bytes using the `serialize` and `deserialize` functions from the `serde` crate.

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
struct Person {
    name: String,
    age: u8,
}

fn main() {
    let person = Person {
        name: String::from("John"),
        age: 30,
    };

    let bytes = bincode::serialize(&person).unwrap();
    println!("{:?}", bytes);
}
```

## Output example

```
[8, 74, 111, 104, 110, 0, 0, 0, 30]
```

## Code explanation


1. `use serde::{Serialize, Deserialize};` - imports the `Serialize` and `Deserialize` traits from the `serde` crate.
2. `#[derive(Serialize, Deserialize)]` - derives the `Serialize` and `Deserialize` traits for the `Person` struct.
3. `let bytes = bincode::serialize(&person).unwrap();` - serializes the `person` struct into a byte array using the `bincode` crate.
4. `println!("{:?}", bytes);` - prints the byte array.

## Helpful links

- [serde](https://crates.io/crates/serde)
- [bincode](https://crates.io/crates/bincode)

group: rust-struct