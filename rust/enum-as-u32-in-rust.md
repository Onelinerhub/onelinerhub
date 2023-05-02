# Enum as u32 in Rust
// plain

Enum in Rust is a type that allows you to define a set of named constants. You can use the `as u32` syntax to convert an enum to a 32-bit unsigned integer. This is useful when you need to store an enum in a database or pass it to a function that requires a number. To do this, you must first define the enum and then use the `as u32` syntax to convert it. For example:
```rust
enum Color {
    Red,
    Green,
    Blue,
}

let color = Color::Red;
let color_as_u32 = color as u32;
```
In this example, the `color_as_u32` variable will contain the value `0` since `Red` is the first value in the enum.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Primitive Types](https://doc.rust-lang.org/book/ch03-02-data-types.html#scalar-types)
- [Rust Casting](https://doc.rust-lang.org/book/ch06-02-match.html#casting-values-to-other-types)

group: rust-enums