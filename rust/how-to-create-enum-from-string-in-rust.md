# How to create enum from string in Rust
// plain

Enums in Rust can be created from strings using the `FromStr` trait. This trait is implemented for the `str` type, allowing us to convert a string into an enum. To do this, we must first define the enum and implement the `FromStr` trait for it. Then, we can use the `str::parse` method to convert a string into the enum.
```rust
use std::str::FromStr;

#[derive(Debug)]
enum Color {
    Red,
    Green,
    Blue,
}

impl FromStr for Color {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "Red" => Ok(Color::Red),
            "Green" => Ok(Color::Green),
            "Blue" => Ok(Color::Blue),
            _ => Err(()),
        }
    }
}

fn main() {
    let color = "Green".parse::<Color>().unwrap();
    println!("{:?}", color);
}
```

Output example:
```
Green
```

## Explanation
 The `FromStr` trait is implemented for the `str` type, allowing us to convert a string into an enum. To do this, we must first define the enum and implement the `FromStr` trait for it. Then, we can use the `str::parse` method to convert a string into the enum. In the example above, we define an enum `Color` with three variants, and implement the `FromStr` trait for it. We then use the `str::parse` method to convert the string "Green" into the `Color` enum.

## Helpful links
- [Rust Documentation - FromStr](https://doc.rust-lang.org/std/str/trait.FromStr.html)
- [Rust Documentation - str::parse](https://doc.rust-lang.org/std/str/fn.parse.html)
- [Rust by Example - Enums](https://doc.rust-lang.org/rust-by-example/custom_types/enum.html)

group: rust-enums