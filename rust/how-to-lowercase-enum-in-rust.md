# How to lowercase enum in Rust
// plain

To lowercase an enum in Rust, you can use the `to_lowercase()` method on the `str` representation of the enum. This method is part of the `std::string::String` module. For example:
```rust
enum Color {
    Red,
    Blue,
    Green,
}

let color = Color::Red;
let lowercase_color = color.to_string().to_lowercase();

println!("{}", lowercase_color);
```
This will output `red`.

Detailed ## Explanation
 The `to_string()` method is used to convert the enum to a `String` type, which is then used to call the `to_lowercase()` method. This method will convert all characters in the `String` to lowercase.

## Helpful links
- [Rust Documentation - Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Documentation - Strings](https://doc.rust-lang.org/std/string/struct.String.html)
- [Rust Documentation - to_lowercase()](https://doc.rust-lang.org/std/primitive.str.html#method.to_lowercase)

group: rust-enums