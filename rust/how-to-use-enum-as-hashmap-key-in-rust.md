# How to use enum as hashmap key in Rust
// plain

Enums in Rust can be used as hashmap keys by implementing the `Eq` and `Hash` traits. This can be done by adding `#[derive(Eq, Hash)]` to the enum definition. For example:
```rust
#[derive(Eq, Hash)]
enum Color {
    Red,
    Blue,
    Green,
}

fn main() {
    use std::collections::HashMap;

    let mut colors = HashMap::new();
    colors.insert(Color::Red, "red");
    colors.insert(Color::Blue, "blue");
    colors.insert(Color::Green, "green");

    println!("{:?}", colors);
}
```

The output of this code is `{Color::Red: "red", Color::Blue: "blue", Color::Green: "green"}`. The `#[derive(Eq, Hash)]` annotation allows the enum to be used as a key in the hashmap.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
- [Rust Derive](https://doc.rust-lang.org/reference/attributes/derive.html)

group: rust-enums