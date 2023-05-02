# Enum as u8 in Rust
// plain

Enum as u8 in Rust is a way to represent an enumeration as a 8-bit unsigned integer. This is useful when you need to store a value in a single byte, such as when working with hardware. To do this, you can use the #[repr(u8)] attribute on the enum. This will cause the compiler to represent the enum as a u8. For example:
```rust
#[repr(u8)]
enum Color {
    Red,
    Green,
    Blue,
}
```
This will cause the compiler to represent the enum as a u8, with Red being 0, Green being 1, and Blue being 2. The output of this code would be:
```
output example
Color::Red as u8 is 0
Color::Green as u8 is 1
Color::Blue as u8 is 2
```
The #[repr(u8)] attribute is useful when you need to store a value in a single byte, such as when working with hardware. It is important to note that the enum values must be in the range of 0 to 255 for this to work.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust repr attribute](https://doc.rust-lang.org/reference/attributes/type_system.html#the-repr-attribute)
- [Rust u8 type](https://doc.rust-lang.org/std/primitive.u8.html)

group: rust-enums