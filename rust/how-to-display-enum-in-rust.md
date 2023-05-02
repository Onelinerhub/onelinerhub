# How to display enum in Rust
// plain

Enums in Rust can be displayed using the `println!` macro. To do this, the enum must first be declared with the `enum` keyword. For example, the following code creates an enum called `Color` with three variants: `Red`, `Green`, and `Blue`:
```rust
enum Color {
    Red,
    Green,
    Blue,
}
```
The enum can then be printed using the `println!` macro, as shown below:
```rust
println!("{:?}", Color::Red);
```
This will output the following:
```
Red
```
The `println!` macro uses the `Display` trait to print the enum, which is why the `{:?}` is used. This allows the enum to be printed in a readable format.

## Helpful links
- [Rust Enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
- [Rust println! macro](https://doc.rust-lang.org/std/macro.println.html)
- [Rust Display trait](https://doc.rust-lang.org/std/fmt/trait.Display.html)

group: rust-enums