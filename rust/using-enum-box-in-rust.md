# Using enum box in Rust
// plain

Enums in Rust are a type of data structure that allows you to define a set of named constants. They are useful for representing a fixed set of values, such as the days of the week or the suits in a deck of cards.

Example code:
```rust
enum Suit {
    Spades,
    Hearts,
    Diamonds,
    Clubs
}

let my_card = Suit::Spades;
```

Output:
```rust
Suit::Spades
```

Code parts with detailed explanation:
- `enum Suit`: This defines a new enum type called `Suit`.
- `Spades`, `Hearts`, `Diamonds`, `Clubs`: These are the four constants that make up the `Suit` enum.
- `let my_card = Suit::Spades`: This creates a variable called `my_card` and assigns it the value of `Suit::Spades`.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Enum Variants](https://doc.rust-lang.org/book/ch06-02-match.html#matching-on-enum-variants)

group: rust-box