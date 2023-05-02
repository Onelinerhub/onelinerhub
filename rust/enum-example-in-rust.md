# Enum example in Rust
// plain

Enums in Rust are a way to define a type by enumerating its possible variants. They are useful for representing a fixed set of values, such as the four suits in a deck of cards. An example of an enum in Rust is the following:
```rust
enum Suit {
    Spades,
    Hearts,
    Diamonds,
    Clubs,
}
```
### Output example
This code does not produce any output.
### Explanation
The `enum` keyword is used to declare an enum type. The type is named `Suit` and it has four variants: `Spades`, `Hearts`, `Diamonds`, and `Clubs`. Each variant is separated by a comma.
### Relevant links
[Enums in the Rust Book](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
[Enums in the Rust Reference](https://doc.rust-lang.org/reference/items/enumerations.html)
[Enums in the Rust by Example](https://doc.rust-lang.org/rust-by-example/custom_types/enum.html)

group: rust-enums