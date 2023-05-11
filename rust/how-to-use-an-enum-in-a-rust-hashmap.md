# How to use an enum in a Rust HashMap?
// plain

Enums can be used as keys in a Rust HashMap. To do this, the enum must implement the `Eq` and `Hash` traits.

## Example code

```rust
use std::collections::HashMap;

#[derive(Eq, Hash, PartialEq)]
enum Color {
    Red,
    Blue,
    Green,
}

fn main() {
    let mut colors = HashMap::new();
    colors.insert(Color::Red, "red");
    colors.insert(Color::Blue, "blue");
    colors.insert(Color::Green, "green");

    println!("{:?}", colors);
}
```

## Output example

```
{Color::Red: "red", Color::Blue: "blue", Color::Green: "green"}
```

## Code explanation


1. `#[derive(Eq, Hash, PartialEq)]`: This line is used to derive the `Eq`, `Hash`, and `PartialEq` traits for the `Color` enum. This is necessary for the enum to be used as a key in a HashMap.

2. `let mut colors = HashMap::new();`: This line creates a new empty HashMap.

3. `colors.insert(Color::Red, "red");`: This line inserts a key-value pair into the HashMap. The key is the `Color::Red` enum variant, and the value is the string `"red"`.

## Helpful links

- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Enum documentation](https://doc.rust-lang.org/book/ch06-00-enums.html)

group: rust-hashmap

onelinerhub: [How to use an enum in a Rust HashMap?](https://onelinerhub.com/rust/how-to-use-an-enum-in-a-rust-hashmap)