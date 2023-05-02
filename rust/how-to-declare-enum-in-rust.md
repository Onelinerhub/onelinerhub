# How to declare enum in Rust
// plain

Enums in Rust are declared using the `enum` keyword, followed by the name of the enum and a set of variants in curly braces. Each variant can optionally have associated data, such as a string or integer. For example, the following code declares an enum called `Color` with three variants: `Red`, `Green`, and `Blue`. Each variant has an associated integer value.
```rust
enum Color {
    Red = 0,
    Green = 1,
    Blue = 2,
}
```
The code above will create an enum with three variants, each with an associated integer value. The output of this code will be a type called `Color` that can be used to store values of type `Color`.

```
output example
Color
```
The enum can then be used to store values of type `Color` in a variable. For example, the following code creates a variable called `my_color` and assigns it the value `Color::Red`.

```rust
let my_color = Color::Red;
```

The enum can also be used to match against values. For example, the following code will print out a message depending on the value of `my_color`.

```rust
match my_color {
    Color::Red => println!("The color is red"),
    Color::Green => println!("The color is green"),
    Color::Blue => println!("The color is blue"),
}
```

Output example:
```
The color is red
```

Enums in Rust are a powerful tool for creating types that can store multiple values. They can be used to store values of a specific type, as well as to match against values.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [Rust Match](https://doc.rust-lang.org/book/ch06-02-match.html)
- [Rust Enum Variants](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html#enum-variants)

group: rust-enums