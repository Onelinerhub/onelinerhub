# How to use an enum as a key in a Rust HashMap?
// plain

Enums can be used as keys in a Rust HashMap by implementing the `Eq` and `Hash` traits.

```rust
use std::collections::HashMap;

#[derive(Eq, Hash, PartialEq)]
enum Color {
    Red,
    Blue,
    Green,
}

fn main() {
    let mut map = HashMap::new();
    map.insert(Color::Red, "red");
    map.insert(Color::Blue, "blue");
    map.insert(Color::Green, "green");

    println!("{:?}", map);
}
```

## Output example

```
{Color::Red: "red", Color::Blue: "blue", Color::Green: "green"}
```

## Code explanation


1. `#[derive(Eq, Hash, PartialEq)]`: This line is used to derive the `Eq` and `Hash` traits for the `Color` enum. This allows the enum to be used as a key in a HashMap.

2. `map.insert(Color::Red, "red")`: This line inserts a key-value pair into the HashMap. The key is the `Color::Red` enum and the value is the string `"red"`.

## Helpful links

- [Rust HashMap documentation](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Eq trait documentation](https://doc.rust-lang.org/std/cmp/trait.Eq.html)
- [Rust Hash trait documentation](https://doc.rust-lang.org/std/hash/trait.Hash.html)

group: rust-hashmap

onelinerhub: [How to use an enum as a key in a Rust HashMap?](https://onelinerhub.com/rust/how-to-use-an-enum-as-a-key-in-a-rust-hashmap)