# How to borrow enum in Rust
// plain

Enums in Rust are used to define a set of named constants. They can be used to create a type-safe set of values that can be used in a program. To borrow an enum in Rust, you can use the `std::borrow::Borrow` trait. This trait allows you to borrow an enum from a type that implements the `std::borrow::Borrow` trait.

## Example code

```rust
use std::borrow::Borrow;

enum Color {
    Red,
    Blue,
    Green,
}

fn main() {
    let color = Color::Red;
    let borrowed_color = color.borrow();
    println!("{:?}", borrowed_color);
}
```

## Output example

```
Red
```

## Code explanation


1. `use std::borrow::Borrow;`: This imports the `Borrow` trait from the `std::borrow` module. This trait is used to borrow an enum from a type that implements the `Borrow` trait.

2. `enum Color { Red, Blue, Green }`: This defines an enum called `Color` with three variants: `Red`, `Blue`, and `Green`.

3. `let color = Color::Red;`: This creates a variable called `color` and assigns it the value `Color::Red`.

4. `let borrowed_color = color.borrow();`: This uses the `Borrow` trait to borrow the enum `color` and assign it to the variable `borrowed_color`.

5. `println!("{:?}", borrowed_color);`: This prints the value of `borrowed_color` to the console.

## Helpful links

- [Rust Enums](https://doc.rust-lang.org/book/ch06-00-enums.html)
- [std::borrow::Borrow](https://doc.rust-lang.org/std/borrow/trait.Borrow.html)

group: rust-borrow